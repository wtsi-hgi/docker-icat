#!/usr/bin/env bash
set -euxv -o pipefail

RESPONSES_FILE=$1

# Ensure PostgreSQL has started
service postgresql start

# Setup iRODS
/var/lib/irods/packaging/setup_irods.sh < ${RESPONSES_FILE}

# The configuration is validated in the setup - ain't nobody got time to keep validating it every time iRODS starts!
rm /var/lib/irods/iRODS/scripts/python/validate_json.py
cp /tmp/resources/validate_json.py /var/lib/irods/iRODS/scripts/python/validate_json.py

# Remove the arbitrary sleep which will either slow the process down or fail to wait for long enough.
# `start-irods.sh` shall be responsible from now on for sensibly checking if the service has started
patch /var/lib/irods/iRODS/scripts/perl/irodsctl.pl /tmp/resources/remove-start-delay.diff
