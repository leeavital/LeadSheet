#!/bin/bash

docker build -t leadsheet .
docker run -p 80:5000 -t leadsheet $@
