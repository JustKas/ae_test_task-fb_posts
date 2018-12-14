import config
from utils import routes
from utils.logs import log
from utils.request_helper import Request


class DataProvider:

    @staticmethod
    def get_user_token():
        """
        This is to get person token from config
        :return: token
        """
        log.debug("Requesting Person Token for test user: {}".format(config.user_name))
        return config.access_token

    @staticmethod
    def get_page_id():
        """
        This is to get Test Page ID
        :return: page id
        """
        log.debug("Get Test Page ID")
        header = {
            "Authorization": 'Bearer ' + config.access_token,
        }
        return Request.get(config.base_url, header, routes.me, routes.accounts)["data"][0]["id"]

    @staticmethod
    def get_page_token():
        """
        This is to get access token for Test Page
        :return: page token
        """
        log.debug("Get Page Token for user: {}".format(config.user_name))
        header = {
            "Authorization": 'Bearer ' + config.access_token,
        }
        return Request.get(config.base_url, header, routes.me, routes.accounts)["data"][0]["access_token"]

    # def get_person_token(self, email, password):
    #     """
    #     This is to get JWT person token from Portal
    #     :param email: user email that is in portal database. E.g. email@dev-pro.net
    #     :param password: user password for email.
    #     :return: jwt token
    #     """
    #     log.info("Get Person Token for user: %s", email)
    #     body = {
    #         "Authorization": email,
    #         "password": password
    #     }
    #     return Request.post(self.uri, self.basic_header, body, self.route.token.value)

    # def get_company_access_token(self, company_id, person_token):
    #     """
    #     This is to get JWT access token for specified company from Portal
    #     :param company_id: ID of company. e.g. 578e98111fa261f4867bdf08
    #     :param person_token: JWT person token. Can be obtained with get_person_token method
    #     :return: jwt company access token
    #     """
    #     log.info("Get Access Token for company: %s", company_id)
    #     body = {"company_id": company_id}
    #     headers = self.get_header(person_token)
    #     return Request.post(self.uri, headers, body, self.route.me.value, self.route.access_token.value)
    #
    # def get_site_token(self, site_id, access_code):
    #     """
    #     This is to get JWT site token for specified site from Portal
    #     :param site_id: ID of site. e.g. 57c83f45b47b1c4d93bbe968
    #     :param access_code: Site access code. e.g. 1baa2747-0ba5-44fa-aa1d-4b42f7504f58.
    #     :return: jwt access token
    #     """
    #     log.info("Get Token for Site: %s", site_id)
    #     body = {"site": site_id, "access_code": access_code}
    #     return Request.post(self.uri, self.basic_header, body, self.route.token)

    # --------------------------------------------------------------------
    # My implementation for update user access token
    # def get_fb_token():
    #     url = 'https://graph.facebook.com/oauth/access_token'
    #     payload = {
    #         'grant_type': {'email': 'dancelife87@mail.ru',
    #                        'password': 'Weissbrau87'},
    #         'client_id': '302117253733482',
    #         'client_secret': '6ea3cce486a25ef727010ab60a75b6fc'
    #     }
    #     response = requests.post(url, params=payload)
    #     return response.json()