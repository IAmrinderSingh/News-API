#!/bin/bash
export FLASK_APP=$1
export FLASK_DEBUG=TRUE
python -m flask run
