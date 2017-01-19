FROM mercury/icat:4-base
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

ENV RENCI_URL=https://packages.irods.org

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https

RUN wget -qO - ${RENCI_URL}/irods-signing-key.asc | sudo apt-key add -
RUN echo "deb [arch=amd64] ${RENCI_URL}/apt/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/renci-irods.list
RUN apt-get update

ADD extract-db-settings.sh /tmp/extract-db-settings.sh
ADD install-irods.sh /tmp/install-irods.sh
ADD setup-irods.sh /tmp/setup-irods.sh
ADD responses.txt /tmp/responses.txt

# FIXME: Temp
ENV IRODS_VERSION=4.2.0