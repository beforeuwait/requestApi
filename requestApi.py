# coding=utf-8

from .requestHandler import RequestRequest
from .requestHandler import SessionRequest
from .exceptions import MethodError
from .exceptions import MethodChoiceError
from .exceptions import IsProxyError
from .exceptions import IsSessionError
from .exceptions import ParametersError


class HttpApi:

    def __init__(self):
        super(HttpApi, self).__init__()

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
        if isinstance(kwargs, dict):
            url = kwargs.get('url', None)
            headers = kwargs.get('headers', None)
            cookies = kwargs.get('cookies', None)
            params = kwargs.get('params', None)
            payloads = kwargs.get('payloads')
            method = kwargs.get('method', None)
            is_proxy = kwargs.get('isProxy', 'yes')
            is_session = kwargs.get('isSession', 'no')
            code = kwargs.get('code', None)

            method = method.lower()
            if not method:
                # raise error
                if method not in ('get', 'post'):
                    raise MethodChoiceError
                raise MethodError
            elif is_proxy not in ('yes', 'no'):
                # raise error
                raise IsProxyError
            elif is_session not in ('yes', 'no'):
                # raise error
                raise IsSessionError
            
            # do next 
            if is_session == 'yes':
                api = SessionRequest()
            else:
                api = RequestRequest()
            html = api.run(
                url=url,
                headers=headers,
                params=params,
                payloads=payloads,
                cookies=cookies,
                code=code,
                is_proxy=is_proxy,
                method=method
            )
            return html
        else:
            # raise error
            raise ParametersError
