# coding=utf-8


import requests
from .theUtils import do_cycle_request
from .requestModel import requestModel


class requestRequest(requestModel):

    def __init__(self):
        super(requestRequest, self).__init__()

    @do_cycle_request
    def get_request_proxy(self, url, headers, params=None, cookies=None):
        pass

    @do_cycle_request
    def post_request_proxy(self, url, headers, payloads, cookies=None):
        pass

    @do_cycle_request
    def get_request_no_proxy(self, url, headers, params=None, cookies=None):
        pass

    @do_cycle_request
    def post_request_no_proxy(self, url, headers, payloads, cookies=None):
        pass


class sessionRequest(requestModel):

    def __init__(self):
        super(sessionRequest, self).__init__()

    @do_cycle_request
    def get_session_proxy(self, url, headers, params=None, cookies=None):
        pass
    
    @do_cycle_request
    def post_session_proxy(self, url, headers, payloads, cookies=None):
        pass
    
    @do_cycle_request
    def get_session_no_proxy(self, url, headers, params=None, cookies=None):
        pass
    
    @do_cycle_request
    def post_session_no_proxy(self, url, headers, payloads, cookies=None):
        pass
    
    def cookies_handler(self, cookies):
        # deal cookie
        pass

    