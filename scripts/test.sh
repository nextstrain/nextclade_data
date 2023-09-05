#! /usr/bin/env bash
echo "Building dataset"
./scripts/rebuild
echo "Starting dataset server"
npx serve@latest --cors --listen=tcp://0.0.0.0:27722 data_output/ &
echo "Opening Nextclade"
open -a "Brave Browser.app" -n --args  " https://master.clades.nextstrain.org?dataset-server=http://localhost:27722"
