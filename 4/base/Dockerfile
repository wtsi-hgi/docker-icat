FROM ubuntu:14.04
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    postgresql

ADD install.sh /tmp/install.sh
ADD install-irods.sh /tmp/install-irods.sh
ADD setup-database.sh /tmp/setup-database.sh
ADD setup-irods.sh /tmp/setup-irods.sh
ADD responses.txt /tmp/responses.txt
ADD resources /tmp/resources

EXPOSE 1247

COPY start.sh start.sh
CMD ./start.sh



