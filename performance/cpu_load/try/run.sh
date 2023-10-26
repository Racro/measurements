#!/bin/bash

# running cmd: bash run.sh logs inner_list.json chrome

set -e

SELFPATH=$(dirname $(realpath "$0"))

LOGS=$(realpath "${1}")

mkdir -p ${LOGS}

# wrapper.py assumes that various files are in the same directory
# pushd "${SELFPATH}/../docker" > /dev/null

# source ~/work/pes/pes/bin/activate
# source ~/pes/venv_measure/bin/activate

# while true; do
UUID=$(uuidgen -t)
echo "Starting measurement run '${UUID}' at $(date)"
python3 wrapper.py \
${LOGS}/${UUID}.log
echo "Completed measurement run '${UUID}' at $(date)"
# done

# popd > /dev/null
