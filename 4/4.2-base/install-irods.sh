#!/usr/bin/env bash
set -euxv -o pipefail

if [ -z ${PLATFORM+x} ];
then
    echo "PLATFORM must be set";
fi
if [ -z ${RENCI_URL+x} ];
then
    echo "RENCI_URL must be set";
fi
if [ -z ${IRODS_VERSION+x} ];
then
    echo "IRODS_VERSION must be set";
fi

# Environment variables for use in build
IRODS_SETTINGS_DIRECTORY=/root/.irods
PLATFORM=trusty
TEMP_WORKING_DIRECTORY=/tmp/installing

# Make temp working directory
mkdir -p $TEMP_WORKING_DIRECTORY
cd $TEMP_WORKING_DIRECTORY

wget ${RENCI_URL}/apt/pool/${PLATFORM}/main/i/irods-server/irods-server_${IRODS_VERSION}_amd64.deb
wget ${RENCI_URL}/apt/pool/${PLATFORM}/main/i/irods-database-plugin-postgres/irods-database-plugin-postgres_${IRODS_VERSION}_amd64.deb

dpkg -i irods-server_${IRODS_VERSION}_amd64.deb || true
dpkg -i irods-database-plugin-postgres_${IRODS_VERSION}_amd64.deb || true
apt-get install -fy
# To find out the dependencies beforehand:
# apt-get install binutils
# ar -p irods-server_${IRODS_VERSION}_amd64.deb control.tar.gz | tar -xzO | grep "^Depends:"

# Cleanup
rm -rf $TEMP_WORKING_DIRECTORY