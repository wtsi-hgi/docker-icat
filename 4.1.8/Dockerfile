FROM ubuntu:14.04
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

ADD install.sh /tmp/install.sh
ADD setup-database.sh /tmp/setup-database.sh
ADD setup-irods.sh /tmp/setup-irods.sh
ADD responses.txt /tmp/responses.txt

RUN /tmp/install.sh
RUN /tmp/setup-database.sh /tmp/responses.txt
RUN /tmp/setup-irods.sh /tmp/responses.txt

# The iRODS setup bakes the hostname available at build time into some unknown places, which are then used to define
# where resources are at runtime. Once upon a time, there appears to have been a way to control what got baked during
# the setup: http://wiki.irods.org/index.php/Changing_the_IP_Address. Sadly, this no longer works and I could not find
# an alternative/way of fixing the damage other than this pretty nasty hack.
RUN sed -i "s/irods_host.*/irods_host\": \"localhost\",/g" /var/lib/irods/.irods/irods_environment.json
RUN mkdir /root/.irods
RUN cp /var/lib/irods/.irods/* /root/.irods
RUN service postgresql start && \
    service irods start && \
    iinit irods123 && \
    iadmin modresc demoResc host localhost

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 1247

COPY start.sh start.sh
CMD ./start.sh



