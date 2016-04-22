#!/usr/bin/env bash
set -eu -o pipefail

/etc/init.d/postgresql start

# FIXME: It should be possible to just start the iCAT server. However, for some reason, which I have not had time to
# investigate, the files in `/home/irods/.irods` and `/etc/irods` "disappear" during the Docker build. The solution used
# here is to setup again. Not using `irods_first_setup` due to the arbitrary sleep command used.
#/etc/init.d/irods start
/var/lib/irods/packaging/setup_irods.sh < /tmp/answers
