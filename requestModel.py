# coding=utf-8


class requestModel:

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

    @staticmethod
    def deal_state_code(state_code):
        # 特殊情况
        # 自行重构
        if state_code < 300:
            return True
        else:
            return False
    