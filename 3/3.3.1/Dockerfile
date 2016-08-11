FROM agaveapi/irods:3.3.1
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

ENV HOME=/home/root

ADD start.sh start.sh
ADD start-irods.sh start-irods.sh

# Gives the root user somewhere to call home
RUN mkdir /home/root

# Enables icommands to allow local testing
WORKDIR ${HOME}
ADD .irods .irods
ENV PATH=${PATH}:/home/irods/iRODS/clients/icommands/bin

# Starts iRODS (may cache things to speed up future starts) and creates `.irodsA` file
RUN ./start-irods.sh && echo "rods" | iinit

CMD ./start.sh