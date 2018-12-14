import config
from utils import base_fb
from utils import routes
from utils.data_manager import DataManager
from utils.logs import log
from utils.request_helper import Request
from utils.verify import Verify


class TestPost:
    """
    POST: Publish message
    """

    msg_id = None
    outdated_msg_id = None
    header = None
    body = None
    body_with_outdated_msg = None
    body_with_updated_msg = None

    def setup(self):
        log.info("PRECONDITIONS: Prepare test data")
        self.header = DataManager.get_header_with_profile_data(base_fb.page_header)
        self.body = DataManager.get_body_with_message(config.message)
        self.body_with_outdated_msg = DataManager.get_body_with_message(config.outdated_message)
        self.body_with_updated_msg = DataManager.get_body_with_message(config.updated_message)

        log.info("PRECONDITIONS: Publish new message")
        response = Request.post(config.base_url, self.header, self.body_with_outdated_msg, base_fb.page_id, routes.feed)
        self.outdated_msg_id = response['id']

        log.info("PRECONDITIONS: Done")

    def teardown(self):
        if self.msg_id is not None:
            log.info("POSTCONDITIONS: Clear test data")
            response = Request.delete(config.base_url, base_fb.page_header, self.msg_id)
            log.info("POSTCONDITIONS: Clearing... {}".format(response))
        response = Request.delete(config.base_url, base_fb.page_header, self.outdated_msg_id)
        log.info("POSTCONDITIONS: Clearing... {}".format(response))

    def test_tc2(self):
        log.info("Publish new message")
        response = Request.post(config.base_url, self.header, self.body, base_fb.page_id, routes.feed)
        self.msg_id = response['id']

        log.info("Verify page id '{}' is present in the response".format(base_fb.page_id))
        Verify.contains(base_fb.page_id, response['id'],
                        "The page id '{}' is not present in the response".format(base_fb.page_id))

    def test_tc4(self):
        log.info("Update message")
        Request.post(config.base_url, self.header, self.body_with_updated_msg, self.outdated_msg_id)

        log.info("Get updated message data")
        response = Request.get(config.base_url, base_fb.page_header, self.outdated_msg_id)

        log.info("Verify page id '{}' is present in the response".format(base_fb.page_id))
        Verify.contains(config.updated_message, response['message'],
                        "The updated message text is not equals to '{}'".format(config.updated_message))
