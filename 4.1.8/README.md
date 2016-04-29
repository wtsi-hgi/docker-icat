# iRODS 4.1.8 Server
This is an Docker image of a vanilla iRODS 4.1.8 server that works out of the box.

## Using the container
### Running
To run the container (with iCAT port binding to the host machine):
```bash
docker run -d --name irods -p 1247:1247 mercury/irods:4.1.8
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
