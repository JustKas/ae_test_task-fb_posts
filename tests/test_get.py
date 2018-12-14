import config
from utils import base_fb
from utils import routes
from utils.data_manager import DataManager
from utils.logs import log
from utils.request_helper import Request
from utils.verify import Verify


class TestGet:
    """
    GET: Read published message
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

    def teardown(self):
        log.info("POSTCONDITIONS: Clear test data")
        response = Request.delete(config.base_url, base_fb.page_header, self.msg_id)
        log.info("POSTCONDITIONS: Clearing... {}".format(response))

    def test_tc1(self):
        log.info("Get last message id")
        self.msg_id = Request.get(config.base_url, base_fb.page_header, base_fb.page_id, routes.feed)['data'][0]['id']

        log.info("Get last message data")
        response = Request.get(config.base_url, base_fb.page_header, self.msg_id)

        log.info("Verify last message text equals to '{}'".format(config.message))
        Verify.equals(config.message, response['message'],
                      "The last message text is not equals to '{}'".format(config.message))
