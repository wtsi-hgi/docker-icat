# iRODS 3.3.1 Server
This is an installation of a vanilla [iRODS 3.3.1](https://github.com/irods/irods-legacy) server that works out of the
box.

The image is based off [that by agveapi](https://hub.docker.com/r/agaveapi/irods), with an additional fix for an issue 
in the iCAT setup script ([bad assumption about database startup time]
(https://github.com/irods/irods-legacy/blob/master/iRODS/scripts/perl/irodsctl.pl#L1318)).


## Building the container
### Build commands 
#### From GitHub
```
docker build -t wtsi-hgi/irods:3.3.1 -f 3.3.1/Dockerfile github.com/wtsi-hgi/docker-icat.git
```


## Using the container
### Running
To run the container (with iCAT port binding to the host machine):
```bash
docker run -d --name irods -p 1247:1247 wtsi-hgi/irods:3.3.1
```

### Connecting
The following iRODS users have been setup:
| Username | Password | Zone | Admin |
| --- | --- | --- | --- |
| rods | rods | iplant | Yes |
| testuser | testuser | iplant | No |


The `.irodsEnv` required to connect as the preconfigured 'rods' user is:
```
irodsUserName rods
irodsHost <$DOCKER_HOST>
irodsPort 1247
irodsZone iplant
```


