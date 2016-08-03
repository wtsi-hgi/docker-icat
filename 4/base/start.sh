#!/usr/bin/env bash
set -eu -o pipefail

service postgresql start
service irods start

echo "iRODS server started successfully!"

sleep infinity