import os
from typing import Sequence, Optional, Tuple

from testwithirods.models import IrodsUser


class IrodsSetup:
    """
    Model of iRODS setup that is to be tested.
    """
    def __init__(self, image_name: str, base_image_to_build: Optional[Tuple], location: str,
                 users: Sequence[IrodsUser], superclass: type):
        self.base_image_to_build = base_image_to_build
        self.image_name = image_name
        self.location = location
        self.users = users
        self.superclass = superclass


def _setup_test(setup: IrodsSetup, test_superclass: type):
    """
    Sets up test.
    :param setup: the iRODS setup that is being tested
    :param test_superclass: the superclass of the test to create
    """
    test_class_name_postfix = setup.image_name.split(":")[-1].replace("-", "_")
    class_name = "%s%s" % (test_superclass.__name__[1:], test_class_name_postfix)

    def init(self, *args, **kwargs):
        super(type(self), self).__init__(type(self)._SETUP, *args, **kwargs)

    globals()[class_name] = type(
        class_name,
        (test_superclass,),
        {
            "_SETUP": setup,
            "__init__": init
        }
    )


def create_tests_for_all_icat_setups(test_superclass: type):
    """
    Creates tests for all iCAT setups, where tests should be made to inherit from the given test superclass.
    :param test_superclass: test superclass
    """
    from tests.builds_to_test import builds_to_test

    single_setup_tag = os.environ.get("SINGLE_TEST_SETUP")
    if single_setup_tag is None:
        for _setup in builds_to_test:
            _setup_test(_setup, test_superclass)
    else:
        for _setup in builds_to_test:
            if _setup[1][0] == single_setup_tag:
                _setup_test(_setup, test_superclass)
                break
