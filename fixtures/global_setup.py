import pytest

from utils import base_fb
from utils.logs import log
from utils.data_provider import DataProvider


@pytest.fixture(scope="session")
def pytest_runtest_setup(item):
    """
    Setup test_name_ global pytest variable and headers
    """
    test_name = item.__dict__.get("name").replace("test_", "")
    setattr(item, "test_name_", test_name)


@pytest.fixture(scope="session", autouse=True)
def global_preconditions():
    log.debug("Collecting test data...")

    log.debug("Generating header with user token...")
    base_fb.user_header = {'Authorization': 'Bearer ' + DataProvider.get_user_token()}
    log.debug("Done\n")

    log.debug("Requesting test page data...")
    base_fb.page_id = DataProvider.get_page_id()
    log.debug("Done\n")

    log.debug("Generating header with page token...")
    base_fb.page_header = {'Authorization': 'Bearer ' + DataProvider.get_page_token()}
    log.debug("Done")

    log.debug("Test data have been prepared!\n")