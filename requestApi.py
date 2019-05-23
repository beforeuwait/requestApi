# coding=utf-8

from .requestHandler import RequestRequest
from .requestHandler import SessionRequest
from .requestModel import RequestModel
from .exceptions import MethodError
from .exceptions import MethodChoiceError
from .exceptions import IsProxyError
from .exceptions import IsSessionError
from .exceptions import ParametersError


class HttpApi(RequestModel):

    def __init__(self):
        super(HttpApi, self).__init__()

    def send_args_get_html(self, **kwargs):
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
            html = api.sub_switch().get(is_proxy).get(method)(
                url=url,
                headers=headers,
                params=params,
                payloads=payloads,
                cookies=cookies,
                code=code
            )
            print(api.session.cookies.items())
            return html
        else:
            # raise error
            raise ParametersError
