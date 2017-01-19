#!/usr/bin/env bash
set -euxv -o pipefail

# Install iRODS
/tmp/install-irods.sh

# Setup database
. /tmp/extract-db-settings.sh /tmp/responses.txt
/tmp/setup-database.sh

# Setup iRODS
service postgresql start
/tmp/setup-irods.sh /tmp/responses.txt

# The iRODS setup bakes the hostname available at build time into some unknown places, which are then used to define
# where resources are at runtime. Once upon a time, there appears to have been a way to control what got baked during
# the setup: http://wiki.irods.org/index.php/Changing_the_IP_Address. Sadly, this no longer works and I could not find
# an alternative/way of fixing the damage other than this pretty nasty hack.
echo $(cat /var/lib/irods/.irods/irods_environment.json | jq '.irods_host="localhost"') > /var/lib/irods/.irods/irods_environment.json

# Copy iRODS settings
mkdir /root/.irods
cp /var/lib/irods/.irods/* /root/.irods

# Create iRODS storage resource
iinit irods123
iadmin modresc demoResc host localhost

# Let's just make sure iRODS seems to start okey - best to find issues now (although issues with settings being linked
# to the build container will not be found)!
service irods stop
/root/start-irods.sh

# Make the world a better place
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
