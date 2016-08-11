FROM agaveapi/irods:3.3.1
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

RUN mkdir /home/root
ENV HOME=/home/root

# Enable icommands to allow local testing
WORKDIR $HOME
ADD .irods .irods
ENV PATH=${PATH}:/home/irods/iRODS/clients/icommands/bin

ADD start.sh start.sh
CMD ./start.sh
