import logging

from tests._common import IrodsSetup
from testwithirods.irods_3_controller import Irods3ServerController
from testwithirods.irods_4_controller import Irods4ServerController
from testwithirods.models import IrodsUser

IRODS_4_x_x_BASE = (None, ("mercury/icat:4-base", "4/base"))

builds_to_test = [
    IrodsSetup("mercury/icat:3.3.1", None, "3/3.3.1", [IrodsUser("rods", "iplant", "rods", admin=True)], Irods3ServerController),
    IrodsSetup("mercury/icat:4.1.8", IRODS_4_x_x_BASE, "4/4.1.8", Irods4ServerController.USERS, Irods4ServerController),
    IrodsSetup("mercury/icat:4.1.9", IRODS_4_x_x_BASE, "4/4.1.9", Irods4ServerController.USERS, Irods4ServerController)
]

logging.root.setLevel(logging.DEBUG)
