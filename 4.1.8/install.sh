#!/usr/bin/env bash
set -eu -o pipefail

# Environment variables for use in build
IRODS_SETTINGS_DIRECTORY=/root/.irods
RENCI_URL=ftp://ftp.renci.org
IRODS_VERSION=4.1.8
PLATFORM=ubuntu14
PG_PLUGIN_VERSION=1.8
TEMP_WORKING_DIRECTORY=/tmp/installing

apt-get update
apt-get install -y --no-install-recommends \
    wget \
    postgresql

# Make temp working directory
mkdir -p $TEMP_WORKING_DIRECTORY
cd $TEMP_WORKING_DIRECTORY

# Download iRODS
wget ${RENCI_URL}/pub/irods/releases/${IRODS_VERSION}/${PLATFORM}/irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb
wget ${RENCI_URL}/pub/irods/releases/${IRODS_VERSION}/${PLATFORM}/irods-database-plugin-postgres-${PG_PLUGIN_VERSION}-${PLATFORM}-x86_64.deb

# Install iRODS
# This is going to fail but then the line afterwards will magically fix things so suppressing the failure
dpkg -i irods-runtime-${IRODS_VERSION}-${PLATFORM}-x86_64.deb irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb 2> /dev/null || true
#apt-get -f -y install
dpkg -i irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb irods-database-plugin-postgres-${PG_PLUGIN_VERSION}-${PLATFORM}-x86_64.deb 2> /dev/null || true
apt-get -f -y install

rm -rf $TEMP_WORKING_DIRECTORY