import pytest

from utils.logs import log

pytest_plugins = "fixtures.global_setup"


@pytest.fixture()
def base_setup(request):
    test_name = request.node.test_name_
    log.debug("Start test: '{}'.".format(test_name))

    yield

    pass
