from typing import Optional, Tuple

from useintest.predefined.irods import Irods3ServiceController, Irods4ServiceController


class IcatSetup:
    """
    Model of iRODS setup that is to be tested.
    """
    def __init__(self, image_name: str, base_image_to_build: Optional[Tuple], location: str, superclass: type):
        self.base_image_to_build = base_image_to_build
        self.image_name = image_name
        self.location = location
        self.superclass = superclass

IRODS_4_X_X_BASE = (None, ("mercury/icat:4-base", "4/base"))
IRODS_4_1_X_BASE = (IRODS_4_X_X_BASE, ("mercury/icat:4.1-base", "4/4.1-base"))
IRODS_4_2_X_BASE = (IRODS_4_X_X_BASE, ("mercury/icat:4.2-base", "4/4.2-base"))


setups = {
    IcatSetup("mercury/icat:3.3.1", None, "3/3.3.1", Irods3ServiceController),
    IcatSetup("mercury/icat:4.1.8", IRODS_4_1_X_BASE, "4/4.1.8", Irods4ServiceController),
    IcatSetup("mercury/icat:4.1.9", IRODS_4_1_X_BASE, "4/4.1.9", Irods4ServiceController),
    IcatSetup("mercury/icat:4.1.10", IRODS_4_1_X_BASE, "4/4.1.10", Irods4ServiceController),
    IcatSetup("mercury/icat:4.2.0", IRODS_4_2_X_BASE, "4/4.2.0", Irods4ServiceController)
}
