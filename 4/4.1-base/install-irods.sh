#!/usr/bin/env bash
set -euxv -o pipefail

if [ -z ${RENCI_URL+x} ];
then
    echo "RENCI_URL must be set";
fi
if [ -z ${IRODS_VERSION+x} ];
then
    echo "IRODS_VERSION must be set";
fi
if [ -z ${PG_PLUGIN_VERSION+x} ];
then
    echo "PG_PLUGIN_VERSION must be set";
fi

# Environment variables for use in build
IRODS_SETTINGS_DIRECTORY=/root/.irods
PLATFORM=ubuntu14
TEMP_WORKING_DIRECTORY=/tmp/installing

# Make temp working directory
mkdir -p $TEMP_WORKING_DIRECTORY
cd $TEMP_WORKING_DIRECTORY

# Download iRODS
wget ${RENCI_URL}/pub/irods/releases/${IRODS_VERSION}/${PLATFORM}/irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb
wget ${RENCI_URL}/pub/irods/releases/${IRODS_VERSION}/${PLATFORM}/irods-database-plugin-postgres-${PG_PLUGIN_VERSION}-${PLATFORM}-x86_64.deb

# Install iRODS
dpkg -i irods-runtime-${IRODS_VERSION}-${PLATFORM}-x86_64.deb irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb || true
dpkg -i irods-icat-${IRODS_VERSION}-${PLATFORM}-x86_64.deb irods-database-plugin-postgres-${PG_PLUGIN_VERSION}-${PLATFORM}-x86_64.deb || true
# It is difficult to figure out exactly what the dependencies are of the above commands. It is possible to cheat and
# pipe their errors to null using `2> /dev/null || true` then fix the issues with `apt-get -f -y install`. It is best to
# know the dependencies though so they can be installed cached in the Dockerfile. Even when the correct dependencies are
# installed, the above are never happy and will not exit successfully: this is just being ignored here as I do not know
# how to please the thing...

# Cleanup
rm -rf $TEMP_WORKING_DIRECTORY