#!/usr/bin/env python3
"""Propose reproducible nucleotide definitions for labelled lineage clades.

The script only proposes definitions supported by the representative tree.  It
does not use held-out sequences.  Every rejected or ambiguous lineage is kept
in the report, so curation decisions are visible and repeatable.

Lineage labels are collected both from the representative metadata and from
the supplied NEXUS tree.  The latter preserves labelled internal nodes such as
4II when no representative tip has that exact parent label.
"""
import argparse
import csv
import itertools
import json
import re


class Node:
    def __init__(self, name=""):
        self.name = name
        self.parent = None
        self.children = []


def parse_newick(text):
    """Small Newick parser sufficient for Augur/FastTree output."""
    text = re.sub(r"\[[^]]*\]", "", text).strip().rstrip(";")
    root = Node()
    current, stack, token = root, [], []

    def finish_token():
        nonlocal token
        value = "".join(token).strip().strip("'\"")
        token = []
        if not value:
            return ""
        return value.split(":", 1)[0]

    for char in text:
        if char == "(":
            child = Node()
            child.parent = current
            current.children.append(child)
            stack.append(current)
            current = child
        elif char == ",":
            name = finish_token()
            if name:
                current.name = name
            parent = stack[-1]
            sibling = Node()
            sibling.parent = parent
            parent.children.append(sibling)
            current = sibling
        elif char == ")":
            name = finish_token()
            if name:
                current.name = name
            current = stack.pop()
        else:
            token.append(char)
    name = finish_token()
    if name:
        current.name = name
    # A Newick root normally has one child after parsing the opening parenthesis.
    return root.children[0] if len(root.children) == 1 and not root.name else root


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


def leaves(node):
    if not node.children:
        return [node]
    result = []
    for child in node.children:
        result.extend(leaves(child))
    return result


def ancestors(node):
    result = []
    while node is not None:
        result.append(node)
        node = node.parent
    return result


def mrca(nodes):
    common = set(ancestors(nodes[0]))
    for node in nodes[1:]:
        common.intersection_update(ancestors(node))
    return next(node for node in ancestors(nodes[0]) if node in common)


MUTATION = re.compile(r"^([A-Za-z*\-])(\d+)([A-Za-z*\-])$")
NEXUS_LINEAGE = re.compile(r'lineage="([^"]+)"')


def parse_mutation(value):
    match = MUTATION.match(value)
    return (int(match.group(2)), match.group(1).upper(), match.group(3).upper()) if match else None


def is_member(terminal, lineage):
    if terminal == lineage:
        return True
    if lineage.endswith(tuple("0123456789")) or "." in lineage:
        return terminal.startswith(lineage + ".")
    # Major DENV lineage labels such as 1I own their underscore descendants.
    return terminal.startswith(lineage + "_") or terminal.startswith(lineage + ".")


def path_to(node):
    """Return nodes from the root through ``node`` for state reconstruction."""
    return list(reversed(ancestors(node)))


def mutations_on_incoming_branch(node, node_data):
    """Return mutations on the branch from ``node.parent`` to ``node``.

    Augur stores mutations for an incoming branch under its child-node name in
    node-data.  Restricting candidates to this list prevents markers inherited
    from more ancestral branches from being proposed for a descendant class.
    """
    return [parsed for value in node_data.get(node.name, {}).get("muts", [])
            if (parsed := parse_mutation(value))]


def final_state(leaf, site, node_data):
    state = None
    for node in path_to(leaf):
        for value in node_data.get(node.name, {}).get("muts", []):
            parsed = parse_mutation(value)
            if parsed and parsed[0] == site:
                state = parsed[2]
    return state


def marker_present(leaf, marker, node_data):
    site, ref, alt = marker
    final = final_state(leaf, site, node_data)
    # The candidate itself is on the path to an ingroup leaf, so its alternate
    # state persists unless a later mutation changes this genomic position.
    # A leaf outside the lineage with no event at this site retains the reference
    # state and must therefore not count as marker-positive.
    return final == alt


def leaf_states(root, node_data):
    """Record final mutation states for each tip in one tree traversal."""
    states = {}
    result = {}

    def visit(node):
        previous = {}
        for value in node_data.get(node.name, {}).get("muts", []):
            parsed = parse_mutation(value)
            if parsed:
                site, _ref, alt = parsed
                if site not in previous:
                    previous[site] = states.get(site)
                states[site] = alt
        if node.children:
            for child in node.children:
                visit(child)
        else:
            result[node] = states.copy()
        for site, old in previous.items():
            if old is None:
                del states[site]
            else:
                states[site] = old

    visit(root)
    return result


def choose_markers(candidates, ingroup_mask, outgroup_mask, presence_masks, min_markers, max_markers, min_support, max_outgroup):
    scored = []
    in_count = ingroup_mask.bit_count()
    out_count = outgroup_mask.bit_count()
    for marker in candidates:
        mask = presence_masks(marker)
        in_support = (mask & ingroup_mask).bit_count() / in_count
        out_support = (mask & outgroup_mask).bit_count() / max(1, out_count)
        if in_support >= min_support:
            scored.append((marker, in_support, out_support))
    scored.sort(key=lambda x: (x[2], -x[1], x[0][0], x[0][2]))
    for size in range(min_markers, min(max_markers, len(scored)) + 1):
        for combo in itertools.combinations(scored, size):
            mask = ingroup_mask | outgroup_mask
            for marker, _in_support, _out_support in combo:
                mask &= presence_masks(marker)
            in_support = (mask & ingroup_mask).bit_count() / in_count
            out_support = (mask & outgroup_mask).bit_count() / max(1, out_count)
            if in_support >= min_support and out_support <= max_outgroup:
                # ``scored`` is ordered by individual outgroup support and
                # ingroup coverage. Iterating panel sizes from minimum to
                # maximum therefore gives the most compact usable panel
                # without exhaustive enumeration of all larger panels.
                return combo, in_support, out_support
    return (), 0.0, 0.0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", required=True)
    parser.add_argument("--mutations", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--nexus", required=True,
                        help="Representative NEXUS tree with lineage annotations")
    parser.add_argument("--serotype", required=True)
    parser.add_argument("--clades-output", required=True)
    parser.add_argument("--report-output", required=True)
    parser.add_argument("--min-support", type=float, default=.95)
    parser.add_argument("--min-markers", type=int, default=1)
    parser.add_argument("--max-markers", type=int, default=3)
    parser.add_argument("--max-outgroup-support", type=float, default=.01)
    args = parser.parse_args()
    if args.min_markers < 1 or args.min_markers > args.max_markers:
        parser.error("--min-markers must be at least 1 and no greater than --max-markers")

    root = parse_newick(open(args.tree).read())
    tip_map = {node.name: node for node in leaves(root)}
    payload = json.load(open(args.mutations))
    node_data = payload["nodes"]
    labels = {}
    with open(args.labels, newline="") as handle:
        for row in csv.DictReader(handle):
            if row["serotype"] == args.serotype and row["set"] == "representatives":
                labels[row["sequence"]] = row["lineage"]
    # Parent lineages can be annotations of internal NEXUS nodes without an
    # identically labelled representative tip.  Include them as discovery
    # targets while retaining the representative metadata as the population
    # used for support and specificity calculations.
    nexus_labels = set(NEXUS_LINEAGE.findall(open(args.nexus).read()))
    # Keep Unassigned representatives in the background population. They are
    # not targets for a clade definition, but a proposed marker panel must
    # discriminate a named lineage from them as well as from other lineages.
    observed = [tip_map[name] for name in labels if name in tip_map]
    states_by_leaf = leaf_states(root, node_data)
    observed_index = {node: index for index, node in enumerate(observed)}
    all_observed_mask = (1 << len(observed)) - 1
    cached_masks = {}

    def presence_masks(marker):
        if marker not in cached_masks:
            site, _ref, alt = marker
            cached_masks[marker] = sum(
                1 << index for index, node in enumerate(observed)
                if states_by_leaf[node].get(site) == alt
            )
        return cached_masks[marker]

    missing = sorted(set(labels) - set(tip_map))
    lineages = sorted(
        ({label for label in labels.values() if label != "Unassigned"} |
         {label for label in nexus_labels if label != "Unassigned"}),
        key=lambda x: (x.count("."), x),
    )

    report = []
    accepted = []
    for lineage in lineages:
        ingroup = [tip_map[name] for name, label in labels.items() if name in tip_map and is_member(label, lineage)]
        if not ingroup:
            report.append([lineage, "needs_review", 0, 0, "", "no labelled tips in tree"])
            continue
        ancestor = mrca(ingroup)
        descendants = {node.name for node in leaves(ancestor)}
        expected = {node.name for node in ingroup}
        purity = len(expected) / len(descendants)
        candidates = list(dict.fromkeys(mutations_on_incoming_branch(ancestor, node_data)))
        ingroup_mask = sum(1 << observed_index[node] for node in ingroup)
        outgroup_mask = all_observed_mask & ~ingroup_mask
        combo, support, out_support = choose_markers(candidates, ingroup_mask, outgroup_mask, presence_masks, args.min_markers, args.max_markers, args.min_support, args.max_outgroup_support)
        markers = ",".join(f"{ref}{site}{alt}" for (site, ref, alt), _, _ in combo)
        status = "proposed" if combo and purity >= args.min_support else "needs_review"
        reason = "" if status == "proposed" else f"tree_purity={purity:.3f}; marker_support={support:.3f}; outgroup_support={out_support:.3f}"
        report.append([lineage, status, len(ingroup), len(descendants), markers, reason])
        if status == "proposed":
            accepted.append((lineage, combo))

    with open(args.clades_output, "w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["clade", "gene", "site", "alt"])
        for lineage, combo in accepted:
            for (site, _ref, alt), _support, _out_support in combo:
                writer.writerow([lineage, "nuc", site, alt])
    with open(args.report_output, "w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["lineage", "status", "labelled_members", "mrca_descendants", "markers", "reason"])
        writer.writerows(report)
        for name in missing:
            writer.writerow(["__input__", "needs_review", 0, 0, "", f"labelled sequence absent from tree: {name}"])


if __name__ == "__main__":
    main()
