#!/usr/bin/env bash
set -eu -o pipefail

# Start PostgreSQL
service postgresql start

# Ensures PostgreSQL is ready to accept connections, fixing: https://github.com/wtsi-hgi/docker-icat/issues/1
echo "Waiting for PostgreSQL to start accepting connections"
while true
do
    ready=$(pg_isready || true)
    if [[ "${ready}" == *"accepting connections"* ]];
    then
        break
    fi
    sleep 0.05 || sleep 1
done
echo "PostgreSQL database is accepting connections!"

# Run iRODS start script
service irods start

# irodsctl.pl has been patched to remove the arbitrary sleep - this script is now responsible for checking when the
# service has started
while true
do
    ready=$(service irods status | sed -n '2p' | sed 's/^ *//;s/$//')
    if [ "${ready}" != "No servers running" ];
    then
        break
    fi
    sleep 0.05 || sleep 1
done
echo "iCAT server has started"
