import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module')
def module_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session')
def session_scope():
    """A session scope fixture."""

@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""


def test_1(session_scope, module_scope, func_scope):
    """Test using session, module, and function scope fixtures"""

def test_2(session_scope, module_scope, func_scope):
    """Demo is more fun with multiple test"""


@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo chass scope fixtures."""
    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""
