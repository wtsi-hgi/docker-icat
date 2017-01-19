#!/usr/bin/env bash
set -euxv -o pipefail

RESPONSES_FILE=$1

# iRODS 4.2.X+ setup
python /var/lib/irods/scripts/setup_irods.py < ${RESPONSES_FILE}

# Fix baked in container address
echo $(cat /etc/irods/server_config.json | jq '.catalog_provider_hosts=["localhost"]') > /etc/irods/server_config.json