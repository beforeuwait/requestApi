# coding=utf-8


import requests
from .theUtils import do_cycle_request
from .requestModel import RequestModel
from .real_config import proxy_dyn, timeout


class RequestRequest(RequestModel):

    def __init__(self):
        super(RequestRequest, self).__init__()

    @staticmethod
    @do_cycle_request
    def get_request_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = requests.get(
                                url=url,
                                headers=headers,
                                params=params,
                                cookies=cookies,
                                proxies=proxy_dyn,
                                timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def post_request_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = requests.post(
                                url=url,
                                headers=headers,
                                payloads=payloads,
                                cookies=cookies,
                                proxies=proxy_dyn,
                                timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def get_request_no_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = requests.get(
                                url=url,
                                headers=headers,
                                params=params,
                                cookies=cookies,
                                timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def post_request_no_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = requests.post(
                                url=url,
                                headers=headers,
                                payloads=payloads,
                                cookies=cookies,
                                timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html
    
    def sub_switch(self):
        return self.switcher().get('no')


session = RequestModel.session


class SessionRequest(RequestModel):

    def __init__(self):
        super(SessionRequest, self).__init__()

    @staticmethod
    @do_cycle_request
    def get_session_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = session.get(
                            url=url,
                            headers=headers,
                            params=params,
                            cookies=cookies,
                            proxies=proxy_dyn,
                            timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def post_session_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = session.post(
                            url=url,
                            headers=headers,
                            payloads=payloads,
                            cookies=cookies,
                            proxies=proxy_dyn,
                            timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def get_session_no_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = session.get(
                            url=url,
                            headers=headers,
                            params=params,
                            cookies=cookies,
                            timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html

    @staticmethod
    @do_cycle_request
    def post_session_no_proxy(url, headers, params=None, payloads=None, cookies=None, code=None):
        response = session.post(
                            url=url,
                            headers=headers,
                            payloads=payloads,
                            cookies=cookies,
                            timeout=timeout)
        status_code = response.status_code
        if RequestModel.deal_state_code(status_code):
            if code:
                html = response.content.decode(code)
            else:
                html = response.text
        else:
            html = 'null_html'
        return html
    
    def sub_switch(self):
        return self.switcher().get('yes')
