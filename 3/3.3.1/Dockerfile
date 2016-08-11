FROM agaveapi/irods:3.3.1
MAINTAINER Colin Nolan <hgi@sanger.ac.uk>

ENV HOME=/home/root

# Gives the root user somewhere to call home
RUN mkdir /home/root
WORKDIR ${HOME}

ADD start.sh start.sh
ADD start-irods.sh start-irods.sh

# Enables icommands to allow local testing
ADD .irods .irods
# Note: Could not get this to work correctly when `docker exec` used so went for the more hacky option!
# ENV PATH=${PATH}:/home/irods/iRODS/clients/icommands/bin
RUN ln -s /home/irods/iRODS/clients/icommands/bin/i* /usr/local/bin

# Starts iRODS (may cache things to speed up future starts) and creates `.irodsA` file
RUN ./start-irods.sh && echo "rods" | iinit

CMD ./start.sh


