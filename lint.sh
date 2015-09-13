#!/usr/bin/env bash

set -x
autopep8 --in-place --indent-size=2  src/**/*.py
