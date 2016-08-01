#!/usr/bin/env bash
set -eu -o pipefail

RESPONSES_FILE=$1

# Ensure PostgreSQL has started
service postgresql start

# Setup iRODS
/var/lib/irods/packaging/setup_irods.sh < $RESPONSES_FILE
