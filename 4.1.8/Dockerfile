FROM ubuntu:14.04
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

ADD install.sh /tmp/install.sh
ADD setup-database.sh /tmp/setup-database.sh
ADD setup-irods.sh /tmp/setup-irods.sh
ADD responses.txt /tmp/responses.txt

RUN /tmp/install.sh
RUN /tmp/setup-database.sh /tmp/responses.txt
RUN /tmp/setup-irods.sh /tmp/responses.txt

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 1247

COPY start.sh start.sh
CMD ./start.sh
