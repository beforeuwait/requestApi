# coding=utf-8

import requests


class RequestModel:

    session = requests.Session()

    def get_request_proxy(self, *args):
        # do get request with proxy in request way
        pass
    
    def post_request_proxy(self, *args):
        # do post request with proxy in request way
        pass

    def get_request_no_proxy(self, *args):
        # do get request without proxy in request way
        pass
    
    def post_request_no_proxy(self, *args):
        # do post request without proxy in request way
        pass
    
    def get_session_proxy(self, *args):
        # do get request with proxy in session way
        pass
    
    def post_session_proxy(self, *args):
        # do post request with proxy in session way
        pass
    
    def get_session_no_proxy(self, *args):
        # do get request without proxy in session way
        pass
    
    def post_session_no_proxy(self, *args):
        # do post request without proxy in session
        pass
    
    def send_args_get_html(self, **kwargs):
        # get the args and deal them
        # receive args
        # include [
        #   url: the url which we need to connect
        #   headers: the headers which we use in request headers
        #   cookies: when we need to use cookie to be checked
        #   params:  the get request with args
        #   payloads: the post request with args
        #   method: choose get or post that we need
        #   isProxy: is there any proxy tha we need to use
        #   isSession: request in seesion or request way
        # ]
        pass

    def get_session_cookie(self):
        # return cookie
        return self.session.cookies.items()

    @staticmethod
    def deal_state_code(state_code):
        # 特殊情况
        # 自行重构
        if state_code < 300:
            return True
        else:
            return False
            
    @classmethod
    def switcher(cls):
        return {
            # request with session
            'yes': {
                # request with proxy
                'yes': {
                    'get': cls.get_session_proxy,
                    'post': cls.post_session_proxy,
                },
                # request without proxy
                'no': {
                    'get': cls.get_session_no_proxy,
                    'post': cls.post_session_no_proxy
                }
            },
            # request with out session
            'no': {
                # with proxy
                'yes': {
                    'get': cls.get_request_proxy,
                    'post': cls.post_request_proxy
                },
                # without proxy
                'no': {
                    'get': cls.get_request_no_proxy,
                    'post': cls.post_session_no_proxy
                }
            }
        }

    def cookies_handler(self, cookies):
        # deal cookie
        pass

    def headers_handler(self, session):
        # deal headers
        # like change the referer
        # like change the user_agent
        # even add/delete parameter
        # user define it
        pass