# coding=utf-8

from .requestModel import requestModel


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
            isProxy = kwargs.get('isProxy', None)
            isSession = kwargs.get('isSession', None)
            if not method:
                # raise error
                raise
            elif isProxy not in ('yes', 'no', None):
                # raise error
                raise
            elif isSession not in ('yes', 'no', None):
                # raise error
                raise
            
            # do next 
            
        else:
            # raise error
            raise


