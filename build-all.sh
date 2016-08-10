#!/usr/bin/env bash
set -eu -o pipefail

docker build -t mercury/icat:3.3.1 3/3.3.1

docker build -t mercury/icat:4-base 4/base
docker build -t mercury/icat:4.1.8 4/4.1.8
docker build -t mercury/icat:4.1.9 4/4.1.9