import os
from abc import abstractmethod

from inflection import camelize

from testwithbaton.api import BatonSetup


class BatonSetupContainer():
    """
    Container of a baton setup.
    """
    @property
    @abstractmethod
    def baton_setup(self) -> BatonSetup:
        """
        A baton setup
        :return: baton setup
        """


def _create_test_for_baton_setup(setup: BatonSetup, test_superclass: type):
    """
    Creates tests for single baton setup.
    :param setup: the setup to create test for
    :param test_superclass: the test superclass
    """
    class_name = "%sWithBaton%s" % (test_superclass.__name__, camelize(setup.name[1:].lower()))

    @property
    def baton_setup(self):
        return self._baton_setup

    globals()[class_name] = type(
        class_name,
        (test_superclass,),
        {
            "_baton_setup": setup,
            "baton_setup": baton_setup
        }
    )


def create_tests_for_all_baton_setups(test_superclass: type):
    """
    Creates tests for all baton setups, where tests should be made to inherit from the given test superclass.
    :param test_superclass: test superclass, which must inherit from `BatonSetupContainer`
    """
    single_setup = os.environ.get("SINGLE_TEST_SETUP")
    if single_setup:
        setup = BatonSetup.__dict__[single_setup]
        _create_test_for_baton_setup(setup, test_superclass)
    else:
        for setup in BatonSetup:
            _create_test_for_baton_setup(setup, test_superclass)
