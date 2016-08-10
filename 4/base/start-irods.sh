#!/usr/bin/env bash
set -eu -o pipefail

# Ensure PostgreSQL has started
service postgresql start

# Run iRODS start script
service irods start

# irodsctl.pl has been patched to remove the arbitrary sleep - this script is now responsible for checking when the
# service has started
while true
do
    databaseReady=$(service irods status | sed -n '2p' | sed 's/^ *//;s/$//')
    if [ "${databaseReady}" != "No servers running" ];
    then
        break
    fi
    sleep 0.05 || sleep 1
done
echo "iCAT server has started"
