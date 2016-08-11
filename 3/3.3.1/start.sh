#!/usr/bin/env bash
set -eu -o pipefail

# Start iRODS
./start-irods.sh

# Continue setup as normal
/usr/bin/supervisord