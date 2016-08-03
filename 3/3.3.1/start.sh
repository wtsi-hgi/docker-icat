#!/usr/bin/env bash
set -eu -o pipefail

# Start database
su - irods -c "/home/irods/iRODS/irodsctl --verbose dbstart"

# Fixing issue: https://github.com/irods/irods-legacy/blob/master/iRODS/scripts/perl/irodsctl.pl#L1318
while true
do
    database_ready=$(su - irods -c "/home/irods/iRODS/irodsctl --verbose status" | sed -n '4p' | sed 's/^ *//;s/$//')
    echo $database_ready
    if [ "$database_ready" != "No servers running" ];
    then
        break
    fi
    sleep 0.05 || sleep 1
done
echo "iCAT database has started"

# Continue setup as normal
/usr/bin/supervisord