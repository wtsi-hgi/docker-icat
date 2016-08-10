import logging

from testwithbaton.irods._irods_3_controller import Irods3_3_1ServerController
from testwithbaton.irods._irods_4_controller import Irods4_1_8ServerController, Irods4_1_9ServerController

IRODS_4_x_x_BASE = (None, ("mercury/icat:4-base", "4/base")),


builds_to_test = [
    (None, ("mercury/icat:3.3.1", "3/3.3.1", Irods3_3_1ServerController)),
    # (IRODS_4_x_x_BASE, ("mercury/icat:4.1.8", "4/4.1.8", Irods4_1_8ServerController())),
    # (IRODS_4_x_x_BASE, ("mercury/icat:4.1.9", "4/4.1.9", Irods4_1_9ServerController()))
]

logging.root.setLevel(logging.DEBUG)