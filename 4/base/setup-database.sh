#!/usr/bin/env bash
set -euxv -o pipefail

RESPONSES_FILE=$1

service postgresql start

DBUSER=`tail -n 3 $RESPONSES_FILE | head -n 1`
DBPASS=`tail -n 2 $RESPONSES_FILE | head -n 1`

sudo -u postgres createdb -O postgres "ICAT"
sudo -u postgres psql -U postgres -d postgres -c "CREATE USER $DBUSER WITH PASSWORD '$DBPASS'"
sudo -u postgres psql -U postgres -d postgres -c "GRANT ALL PRIVILEGES ON DATABASE \"ICAT\" TO $DBUSER"
