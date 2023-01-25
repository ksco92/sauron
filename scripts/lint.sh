#!/bin/sh

set -ex

python3 -m black ./src/ --exclude ./src/power_functions/utils/chunk_list.py
python3 -m black ./test/
python3 -B -m isort ./src/ ./test/
python3 -m flake8 --config=setup.cfg ./