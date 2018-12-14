import config
from utils import base_fb
from utils import routes
from utils.data_manager import DataManager
from utils.logs import log
from utils.request_helper import Request
from utils.verify import Verify


class TestDELETE:
    """
    DELETE: Delete published message
    """

    msg_id = None

    def setup(self):
        log.info("PRECONDITIONS: Prepare test data")
        header = DataManager.get_header_with_profile_data(base_fb.page_header)
        body = DataManager.get_body_with_message(config.message)
        log.info("PRECONDITIONS: Publish new message")
        response = Request.post(config.base_url, header, body, base_fb.page_id, routes.feed)
        self.msg_id = response['id']
        log.info("PRECONDITIONS: Done")

    def test_tc3(self):
        log.info("DELETE: Publish new message")
        response = Request.delete(config.base_url, base_fb.page_header, self.msg_id)
        log.debug(response)

        log.info("Verify response consist parameter 'success' with status 'True'")
        Verify.true(response['success'], "The parameter 'success' is not equals to 'True'")
