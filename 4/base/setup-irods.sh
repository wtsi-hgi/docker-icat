#!/usr/bin/env bash
set -eux -o pipefail

RESPONSES_FILE=$1

# Ensure PostgreSQL has started
service postgresql start

# Setup iRODS
/var/lib/irods/packaging/setup_irods.sh < $RESPONSES_FILE

# The configuration is validated in the setup - ain't nobody got time to keep validating it every time iRODS starts!
rm /var/lib/irods/iRODS/scripts/python/validate_json.py
cp /tmp/resources/validate_json.py /var/lib/irods/iRODS/scripts/python/validate_json.py