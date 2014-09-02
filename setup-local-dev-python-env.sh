#!/bin/bash

DIR=`dirname "$0"`
ENV_DIR="$DIR/python-env"
PIP_REQUIREMENT_FILE="$DIR/requirements.txt"

if [ ! -d "$ENV_DIR" ]; then
  mkdir "$ENV_DIR"
  virtualenv --python=python2.7 "$ENV_DIR"
fi
source "$ENV_DIR"/bin/activate
pip install -r "$PIP_REQUIREMENT_FILE"
