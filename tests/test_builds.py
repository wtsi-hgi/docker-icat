import logging
import os
import types
import unittest
from time import sleep
from typing import List, Optional, Tuple, Union

from tests.builds_to_test import builds_to_test
from testwithbaton._common import create_client
from testwithbaton.irods._irods_contoller import IrodsServerController
from testwithbaton.models import ContainerisedIrodsServer

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

    def __init__(self, top_level_image: Tuple[Optional[Tuple], Tuple[str, str]], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._top_level_image = top_level_image

    def setUp(self):
        type(self)._build_image(self._top_level_image)
        ServerController = self._create_server_controller(self._top_level_image[1][2], self._top_level_image[1][0])
        self.server_controller = ServerController()

    # TODO: Test stop

    def test_icommands_installed(self):
        # response = self._run(command="ienv", environment={"DEBUG": 1}, stderr=False)
        # self.assertIn("Release Version = rods", response)
        # print(self._run("ils"))
        container = self.server_controller.start_server()
        try:
            test_file_name = "test123"
            self._run(["touch", test_file_name], container)
            self._run(["iput", test_file_name], container)
            self.assertIn(test_file_name, self._run(["ils"], container))
        finally:
            self.server_controller.stop_server(container)


    def _run(self, command: Union[str, List[str]], container: ContainerisedIrodsServer) -> str:
        """
        TODO

        Run the containerised baton image that is been tested.
        """
        container_id = container.native_object["Id"]
        docker_client = create_client()
        id = docker_client.exec_create(container_id, cmd=command)
        chunks = []
        for chunk in docker_client.exec_start(id, stream=True):
            logging.debug(chunk)
            chunks.append(chunk.decode("utf-8"))
        return "".join(chunks)


    @staticmethod
    def _create_server_controller(controller_base_class: type, image: str) -> IrodsServerController:
        """
        TODO
        :param controller_base_class:
        :param image:
        :return:
        """
        def start_server(controller: IrodsServerController) -> ContainerisedIrodsServer:
            return controller._start_server(image, controller_base_class.VERSION, controller_base_class.USERS)

        return type(
            "TODO",
            (controller_base_class, ),
            {
                "start_server": start_server
            }
        )


def _setup_test_for_build(setup):
    """
    TODO
    :param setup:
    :return:
    """
    test_class_name_postfix = setup[1][0].split(":")[-1].replace("-", "_")
    class_name = "%s%s" % (_TestICAT.__name__[1:], test_class_name_postfix)

    def init(self, *args, **kwargs):
        super(type(self), self).__init__(type(self)._SETUP, *args, **kwargs)

    globals()[class_name] = type(
        class_name,
        (_TestICAT,),
        {
            "_SETUP": setup,
            "__init__": init
        }
    )

single_setup_tag = os.environ.get("SINGLE_TEST_SETUP")
if single_setup_tag is None:
    for _setup in builds_to_test:
        _setup_test_for_build(_setup)
else:
    for _setup in builds_to_test:
        if _setup[1][0] == single_setup_tag:
            _setup_test_for_build(_setup)
            break


# Stop unittest from running the abstract base test
del _TestICAT


if __name__ == "__main__":
    unittest.main()
