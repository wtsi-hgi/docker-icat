#!/usr/bin/env bash
set -eu -o pipefail

# Install iRODS
/tmp/install-irods.sh

# Setup
/tmp/setup-database.sh /tmp/responses.txt
/tmp/setup-irods.sh /tmp/responses.txt

# The iRODS setup bakes the hostname available at build time into some unknown places, which are then used to define
# where resources are at runtime. Once upon a time, there appears to have been a way to control what got baked during
# the setup: http://wiki.irods.org/index.php/Changing_the_IP_Address. Sadly, this no longer works and I could not find
# an alternative/way of fixing the damage other than this pretty nasty hack.
sed -i "s/irods_host.*/irods_host\": \"localhost\",/g" /var/lib/irods/.irods/irods_environment.json
mkdir /root/.irods
cp /var/lib/irods/.irods/* /root/.irods
# Asserting that postgresql and irods have been started during their setup
iinit irods123
iadmin modresc demoResc host localhost

# Make the world a better place
apt-get clean
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
