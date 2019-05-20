# coding=utf-8


import requests
from .theUtils import do_cycle_request
from .requestModel import requestModel
from .config import proxy_dyn, timeout

class requestRequest(requestModel):

    def __init__(self):
        super(requestRequest, self).__init__()

    @do_cycle_request
    def get_request_proxy(self, url, headers, params=None, payloads=None, cookies=None):
        response = requests.get(url=url, 
                                headers=headers,
                                params=params,
                                cookies=cookies,
                                proxies=proxy_dyn,
                                timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')

    @do_cycle_request
    def post_request_proxy(self, url, headers, params=None, payloads=None, cookies=None):
        response = requests.post(url=url, 
                                headers=headers,
                                payloads=payloads,
                                cookies=cookies,
                                proxies=proxy_dyn,
                                timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')

    @do_cycle_request
    def get_request_no_proxy(self, url, headers, params=None, payloads=None, cookies=None):
        response = requests.get(url=url, 
                                headers=headers,
                                params=params,
                                cookies=cookies,
                                timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')

    @do_cycle_request
    def post_request_no_proxy(self, url, headers, params=None, payloads=None, cookies=None):
        response = requests.post(url=url, 
                                headers=headers,
                                payloads=payloads,
                                cookies=cookies,
                                timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')
    
    def sub_switch(self):
        return self.switcher().get('no')


class sessionRequest(requestModel):

    def __init__(self):
        super(sessionRequest, self).__init__()
        self.session = requests.session()

    @do_cycle_request
    def get_session_proxy(self, url, headers, params=None, cookies=None):
        response = self.session.get(url=url, 
                                    headers=headers,
                                    params=params,
                                    cookies=cookies,
                                    proxies=proxy_dyn,
                                    timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')
    
    @do_cycle_request
    def post_session_proxy(self, url, headers, payloads=None, cookies=None):
        response = self.session.post(url=url, 
                                    headers=headers,
                                    payloads=payloads,
                                    cookies=cookies,
                                    proxies=proxy_dyn,
                                    timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')
    
    @do_cycle_request
    def get_session_no_proxy(self, url, headers, params=None, cookies=None):
        response = self.session.get(url=url, 
                                    headers=headers,
                                    params=params,
                                    cookies=cookies,
                                    timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')
    
    @do_cycle_request
    def post_session_no_proxy(self, url, headers, payloads=None, cookies=None):
        response = self.session.post(url=url, 
                                    headers=headers,
                                    payloads=payloads,
                                    cookies=cookies,
                                    timeout=timeout)
        state_code = response.state_code
        if self.deal_state_code(state_code):
            return (True, response.content)
        else:
            return (False, 'null_html')
    
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
    
    def sub_switch(self):
        return self.switcher().get('yes')

    