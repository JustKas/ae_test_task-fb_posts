import json
import requests

from utils.common_actions import CommonActions as CA
from utils.logs import log


class Request:

    @staticmethod
    def post(url, headers, body, *routes):
        request_url = CA.format_url(url, *routes)
        log.debug("POST: %s", request_url)
        log.debug("HEADERS: %s", headers)
        log.debug("BODY: %s", body)
        response = requests.post(url=request_url, json=body, headers=headers)
        if 200 <= response.status_code <= 206:
            return json.loads(str(response.content, 'utf-8'))
        else:
            raise ResponseException(str(response.content, 'utf-8'))

    @staticmethod
    def get(url, headers, *routes):
        request_url = CA.format_url(url, *routes)
        log.debug("GET: %s", request_url)
        log.debug("HEADERS: %s", headers)
        response = requests.get(url=request_url, headers=headers)
        if response.status_code is 200:
            return json.loads(str(response.content, 'utf-8'))
        else:
            raise ResponseException(str(response.content, 'utf-8'))

    @staticmethod
    def delete(url, headers, *routes):
        request_url = CA.format_url(url, *routes)
        log.debug("DELETE: %s", request_url)
        log.debug("HEADERS: %s", headers)
        response = requests.delete(url=request_url, headers=headers)
        if 200 <= response.status_code <= 206:
            return json.loads(str(response.content, 'utf-8'))
        else:
            raise ResponseException(str(response.content, 'utf-8'))

    @staticmethod
    def put(url, headers, body, *routes):
        request_url = CA.format_url(url, *routes)
        log.debug("PUT: %s", request_url)
        log.debug("HEADERS: %s", headers)
        log.debug("BODY: %s", body)
        response = requests.put(url=request_url, json=body, headers=headers)
        if 200 <= response.status_code <= 206:
            return json.loads(str(response.content, 'utf-8'))
        else:
            raise ResponseException(str(response.content, 'utf-8'))


class ResponseException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)