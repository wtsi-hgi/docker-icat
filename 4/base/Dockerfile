FROM ubuntu:14.04
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    postgresql \
    ca-certificates \
    libfuse2 \
    libjson-perl \
    lsof \
    python-chardet \
    python-jsonschema \
    python-psutil \
    python-requests \
    python2.7 \
    super \
    unixodbc \
    sudo \
    odbc-postgresql \
    patch \
    jq

ADD install.sh /tmp/install.sh
ADD setup-database.sh /tmp/setup-database.sh
ADD resources /tmp/resources

EXPOSE 1247

WORKDIR /root
ADD start-irods.sh start-irods.sh
ADD start.sh start.sh
CMD ./start.sh



