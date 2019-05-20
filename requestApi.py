# coding=utf-8

from .requestModel import requestModel
from .exceptions import MethodError
from .exceptions import IsProxyError
from .exceptions import IsSessionError
from .exceptions import ParametersError


class httpApi(requestModel):
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
            method = method.lower()
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
        else:
            # raise error
            raise ParametersError
        
    def switcher(self):
        return  {
            'yes': {
                'yes': {
                    'get': self.get_session_proxy,
                    'post': self.post_session_proxy,
                },
                'no': {
                    'get': self.get_session_no_proxy,
                    'post': self.post_session_no_proxy
                }
            },
            'no': {
                'yes':{
                    'get': self.get_request_proxy,
                    'post': self.post_request_proxy
                },
                'no': {
                    'get': self.get_request_no_proxy,
                    'post': self.post_session_no_proxy
                }
            }
        }

