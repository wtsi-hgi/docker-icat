#!/usr/bin/env bash
set -eu -o pipefail

# Start database and iRODS
su - irods -c "/home/irods/iRODS/irodsctl --verbose start"

# Fixing issue: https://github.com/irods/irods-legacy/blob/master/iRODS/scripts/perl/irodsctl.pl#L1318
while true
do
    ready=$(su - irods -c "/home/irods/iRODS/irodsctl --verbose status" | sed -n '2p' | sed 's/^ *//;s/$//')
    if [ "${ready}" != "No servers running" ];
    then
        break
    fi
    sleep 0.05 || sleep 1
done
echo "iCAT database and server has started"
