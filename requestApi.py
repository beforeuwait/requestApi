# coding=utf-8

from .requestHandler import requestRequest
from .requestHandler import sessionRequest
from .exceptions import MethodError
from .exceptions import IsProxyError
from .exceptions import IsSessionError
from .exceptions import ParametersError


class httpApi():
    def __init__(self):
        super(httpApi, self).__init__()

    def send_args_get_html(self, **kwargs):
        if isinstance(kwargs, dict):
            url = kwargs.get('url', None)
            headers = kwargs.get('headers', None)
            cookies = kwargs.get('cookies', None)
            params = kwargs.get('params', None)
            payloads = kwargs.get('payloads')
            method = kwargs.get('method', None)
            isProxy = kwargs.get('isProxy', 'yes')
            isSession = kwargs.get('isSession', 'no')
            if not method:
                # raise error
                raise MemoryError
            elif isProxy not in ('yes', 'no'):
                # raise error
                raise IsProxyError
            elif isSession not in ('yes', 'no'):
                # raise error
                raise IsSessionError
            
            # do next 
            if isSession == 'yes':
                api = sessionRequest()
            else:
                api = requestRequest()
            method = method.lower()
            html = api.sub_switch().get(isProxy).get(method)(
                url=url,
                headers=headers,
                params=params,
                payloads=payloads,
                cookies=cookies)
            print(html)
            """
            if isSession == 'yes':
                if isProxy == 'yes':
                    if method == 'get':
                        self.get_session_proxy()
                    else:
                        self.post_session_proxy()
                else:
                    if method == 'get':
                        self.get_session_no_proxy()
                    else:
                        self.post_session_no_proxy()
            else:
                if isProxy == 'yes':
                    if method == 'get':
                        self.get_request_proxy()
                    else:
                        self.post_request_proxy()
                else:
                    if method == 'get':
                        self.get_request_no_proxy()
                    else:
                        self.post_request_no_proxy()
            """
        else:
            # raise error
            raise ParametersError
        
