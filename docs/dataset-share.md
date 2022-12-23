# Sharing a dataset with the community

This guide assumes that you have created a new dataset to allow Nextclade to perform analysis of sequences for a new pathogen, and that now you want to share your dataset with scientific community, to allow other people to perform such analysis as well.

This guide assumes you have some basic knowledge about Nextclade and is capable of using either Nextclade Web, Nextclade CLI or both. If it's not the case, please refer to [Nextclade user documentation](https://docs.nextstrain.org/projects/nextclade/en/stable/index.html).

There are multiple options (ordered by increasing complexity and level of customization):

- Using a dataset locally yourself and sending it to your friends and colleagues for usage on their computers
- Hosting a single dataset on the internet on your own
- Including a dataset or a family of datasets into the index of official datasets (https://data.clades.nextstrain.org/index_v2.json)
- Hosting your own dataset server (your own dataset index, with one or many datasets)

### Using a dataset locally yourself and sending it to your friends and colleagues for usage on their computers

Once you have a directory of files for a single dataset, it's ready to be used locally, and it requires no additional preparation. However, this option only allows to use the dataset on your computer (or on any computer which has a copy of the dataset directory).

#### Using local dataset in Nextclade CLI

You can tell Nextclade CLI to use your new dataset, just as with any other dataset, by passing the path to your dataset directory into the `--input-dataset` CLI argument of the `nextclade run` command.

#### Using local dataset in Nextclade Web

It is possible to serve the dataset directory locally using a file server and to use it in Nextclade Web. You can use any local file server software (But make sure that [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is enabled on your server). For example, if you have Node.js installed, you could use [serve](https://www.npmjs.com/package/serve) package to serve the directory locally:

```bash
npx serve --cors --listen=tcp://0.0.0.0:27722 <path_to_your_dataset_dir>
```

In this case, the files will be accessible at `http://localhost:27722`. You then you can pass the local URL to the `dataset-url` query URL parameter of Nextclade Web:

```
https://clades.nextstrain.org?dataset-url=http://localhost:27722
```

This should open Nextclade Web and load your local dataset (instead of allowing to choose among default datasets), so that you can run the analysis for the new pathogen right away.

You can of course zip the directory and share it with your friends and colleagues, e.g. in an email or using a Google Drive, GitHub or any other file hosting.

This option is also useful to test and debug your dataset as you are creating and refining it.

### Hosting a dataset on the internet on your own

Once you have a directory of files for a single dataset ready, you can host the files not only locally (as in previous section), but also on the internet. This way you can make a single dataset remotely accessible to the community, but they will need to take additional steps in order to use it.

In order to host a dataset, you can use any static file web server (e.g. Apache, Nginx), a cloud hosting service (e.g. AWS S3, Google Cloud Storage), or on a version control service (e.g. GitHub, GitLab). Make sure that [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is enabled on your server. A GitHub repository can also act as a web server.

#### Using remote dataset in Nextclade Web

You need to communicate the URL to the dataset directory to your target audience (e.g. your company or a lab). They can then point Nextclade Web to your dataset, by passing your dataset URL to `dataset-url` URL param:

```
https://clades.nextstrain.org?dataset-url=https://my-dataset-server.com/path/to/my-dataset-dir
```

The `dataset-url` param can accept full URLs and also special shortcuts. Read more in [documentation of URL parameters in Nextclade Web](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-web.html#url-parameters).

#### Using remote dataset in Nextclade CLI

For Nextclade CLI, there is no mechanism to download a single custom dataset. Instead, you could provide users with a URL to a zip archive containing all the dataset files. They would then download the zip (manually, or for example using `curl`) and pass a path to it into the `--input-dataset` argument (Nextclade CLI accepts both - directories and zip archives).

Note that this hosting option only allows sharing a single dataset (for a single pathogen). You can of course host multiple datasets in subdirectories and provide users with separate URLs for each, or instruct users how to modify URLs to switch between datasets:

```
https://clades.nextstrain.org?dataset-url=https://my-dataset-server.com/path/to/my-datasets/first-pathogen
https://clades.nextstrain.org?dataset-url=https://my-dataset-server.com/path/to/my-datasets/second-pathogen
https://clades.nextstrain.org?dataset-url=https://my-dataset-server.com/path/to/my-datasets/<...>
```

This would also work well if you put all the customized URLs to some web page. Users then could click and navigate to Nextclade Web already preconfigured with your dataset.

If you want to allow users to toggle between multiple datasets using Nextclade itself, read the next sections.

### Including a new dataset or a family of related datasets into the index of official datasets

This section describes how to include a new dataset or a family of related datasets into the list of official datasets, by configuring the official Nextclade dataset server to serve your new datasets to the world.

This option allows Nextclade users to see your new datasets in:

- the dataset selector on main page of Nextclade Web
- the output list of `nextclade dataset list` command of Nextclade CLI

The datasets will be shown by default and require no additional steps for the users. This option ensures the broadest adoption, but is reserved only for the highest quality datasets.

> Please note that the project maintainers may not necessarily be experts on a particular pathogen you are interested in, so they not always can judge the quality of datasets, nor necessarily have time to learn the specifics.
>
> If you feel that your dataset deserves being on the main page, then submit it for a review and discussion. It would be nice if you first used the other sharing options to gather some feedback from the community.

### Hosting your own dataset server (your own dataset index, with one or many datasets)

TODO
