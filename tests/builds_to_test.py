import logging

from tests._common import IcatSetup
from useintest.predefined.irods import IrodsUser, Irods3ServiceController, Irods4ServiceController

IRODS_4_x_x_BASE = (None, ("mercury/icat:4-base", "4/base"))

builds_to_test = [
    IcatSetup("mercury/icat:3.3.1", None, "3/3.3.1", Irods3ServiceController),
    IcatSetup("mercury/icat:4.1.8", IRODS_4_x_x_BASE, "4/4.1.8", Irods4ServiceController),
    IcatSetup("mercury/icat:4.1.9", IRODS_4_x_x_BASE, "4/4.1.9", Irods4ServiceController),
    IcatSetup("mercury/icat:4.1.10", IRODS_4_x_x_BASE, "4/4.1.10", Irods4ServiceController)
]

logging.root.setLevel(logging.DEBUG)
