#!/usr/bin/env bash
set -euxv -o pipefail

if [ -z ${DB_NAME+x} ];
then
    echo "DB_NAME must be set";
fi
if [ -z ${DB_USER+x} ];
then
    echo "DB_USER must be set";
fi
if [ -z ${DB_PASS+x} ];
then
    echo "DB_PASS must be set";
fi

service postgresql start

sudo -u postgres createdb -O postgres "${DB_NAME}"
sudo -u postgres psql -U postgres -d postgres -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASS}'"
sudo -u postgres psql -U postgres -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE \"${DB_NAME}\" TO ${DB_USER}"
