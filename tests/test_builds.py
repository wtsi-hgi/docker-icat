import logging
import os
import unittest
from typing import List, Optional, Tuple, Union

import tests
from hgicommon.docker.client import create_client
from hgicommon.helpers import create_random_string
from tests._common import IrodsSetup, create_tests_for_all_icat_setups
from testwithirods.irods_contoller import IrodsServerControllerClassBuilder
from testwithirods.models import ContainerisedIrodsServer, Version

_PROJECT_ROOT = "%s/.." % os.path.dirname(os.path.realpath(__file__))
_DEFAULT_IRODS_PORT = 1247


class _TestICAT(unittest.TestCase):
    """
    Tests for an iCAT setup.
    """
    @staticmethod
    def _build_image(top_level_image: Tuple[Optional[Tuple], Tuple[str, str]]):
        """
        Builds images bottom up, building the top level image last.
        :param top_level_image: representation of the top level image
        """
        image = top_level_image
        images = []     # type: List[Tuple[str, str]]
        while image is not None:
            images.insert(0, image[1])
            image = image[0]

        docker_client = create_client()
        for image in images:
            tag = image[0]
            directory = "%s/%s" % (_PROJECT_ROOT, image[1])
            for line in docker_client.build(tag=tag, path=directory):
                logging.debug(line)

    @staticmethod
    def _run(command: Union[str, List[str]], container: ContainerisedIrodsServer) -> str:
        """
        Run the given commend on the containerised server.
        :param command: the command to run
        :param container: the containerised server to run the command in
        """
        container_id = container.native_object["Id"]
        docker_client = create_client()
        id = docker_client.exec_create(container_id, cmd=command)
        chunks = []
        for chunk in docker_client.exec_start(id, stream=True):
            logging.debug(chunk)
            chunks.append(chunk.decode("utf-8"))
        return "".join(chunks)

    def __init__(self, setup: IrodsSetup, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup = setup

    def setUp(self):
        # XXX: Using random image name to stop caching by `test-with-irods`. However should really clean up these
        # images!
        random_image_name = create_random_string(self._setup.image_name)
        type(self)._build_image((self._setup.base_image_to_build, (random_image_name, self._setup.location)))
        ServerController = IrodsServerControllerClassBuilder(
            self._setup.image_name, Version(self._setup.location.split("/")[-1]),
            self._setup.users, self._setup.superclass).build()
        self.server_controller = ServerController()

    def tearDown(self):
        self.server_controller.tear_down()

    def test_starts(self):
        container = self.server_controller.start_server()
        test_file_name = "test123"
        self._run(["touch", test_file_name], container)
        self._run(["iput", test_file_name], container)
        self.assertIn(test_file_name, self._run(["ils"], container))


# Create tests for all baton versions
create_tests_for_all_icat_setups(_TestICAT)
for name, value in tests._common.__dict__.items():
    if _TestICAT.__name__[1:] in name:
        globals()[name] = value
del _TestICAT


if __name__ == "__main__":
    unittest.main()
