#!/bin/bash
PYTHON_PATH="/usr/irissys/bin/irispython"
set -m
cd ${SRC_PATH}/src/python/person
${PYTHON_PATH} -m gunicorn --bind "0.0.0.0:5000" wsgi:app &  fg %1
