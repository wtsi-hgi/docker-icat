# iRODS 4.1.10 Server
**Not for use in production!**

This is a Docker image of a vanilla iRODS 4.1.10 server that works out of the box.

## Using the container
### Running
To run the container (with iCAT port binding to the host machine):
```bash
docker run -d --name irods -p 1247:1247 mercury/irods:4.1.10
```

### Connecting
The following iRODS users have been setup:
```
| Username | Password | Zone     | Admin |
| -------- | -------- | -------- | ----- |
| rods     | irods123 | testZone | Yes   |
```

The `irods_environment.json` in `~/.irods` required to connect as the preconfigured 'rods' user is:
```
{
    "irods_host": "localhost",
    "irods_port": 1247,
    "irods_user_name": "rods",
    "irods_zone_name": "testZone"
}
```

## Acknowledgments
This image was originally based off [that by gmauro](https://github.com/gmauro/boxed-irods) but then re-written to work
around various issues. It was also influenced by the [iRODS 4.1.3 image]
(https://github.com/irods/contrib/tree/master/irods-docker) in the iRODS community code repository ("contrib").