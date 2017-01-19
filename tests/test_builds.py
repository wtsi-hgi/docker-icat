import logging
import os
import unittest
from abc import ABCMeta
from typing import List, Optional, Tuple, Union

import docker

from hgicommon.docker.client import create_client
from hgicommon.helpers import create_random_string
from hgicommon.testing import create_tests, TestUsingObject, ObjectTypeUsedInTest
from tests._common import setups
from useintest.predefined.irods import build_irods_service_controller_type, IrodsDockerisedService

_PROJECT_ROOT = "%s/.." % os.path.dirname(os.path.realpath(__file__))


class _TestICAT(TestUsingObject[ObjectTypeUsedInTest], metaclass=ABCMeta):
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
    def _run(command: Union[str, List[str]], service: IrodsDockerisedService) -> str:
        """
        Run the given commend on the containerised server.
        :param command: the command to run
        :param service: the containerised service managing the iCAT
        """
        container_id = service.container["Id"]
        docker_client = create_client()
        id = docker_client.exec_create(container_id, cmd=command)
        chunks = []
        for chunk in docker_client.exec_start(id, stream=True):
            logging.debug(chunk)
            chunks.append(chunk.decode("utf-8"))
        return "".join(chunks)

    def setUp(self):
        self.setup = self.get_object_to_test()
        self.test_image_name = create_random_string(self.setup.image_name)
        type(self)._build_image((self.setup.base_image_to_build, (self.test_image_name, self.setup.location)))
        repository, tag = self.test_image_name.split(":")
        ServiceController = build_irods_service_controller_type(repository, tag, self.setup.superclass)
        self.service_controller = ServiceController()
        self.service = self.service_controller.start_service()

    def tearDown(self):
        self.service_controller.stop_service(self.service)
        client = docker.from_env()
        client.images.remove(self.test_image_name, force=True)

    def test_starts(self):
        test_file_name = "test123"
        self._run(["touch", test_file_name], self.service)
        self._run(["iput", test_file_name], self.service)
        self.assertIn(test_file_name, self._run(["ils"], self.service))

# Setup tests
globals().update(create_tests(_TestICAT, setups, lambda superclass, test_object: "TestICATWith%s"
                                                                                 % test_object.location.split("/")[1]))

# Fix for stupidity of test runners
del _TestICAT, TestUsingObject, create_tests

if __name__ == "__main__":
    unittest.main()
