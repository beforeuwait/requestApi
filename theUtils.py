# coding=utf-8

from .config import retry
from copy import deepcopy
import requests

def do_cycle_request(fun):

    def do_request():
        html = None
        retryc = deepcopy(retry)
        while retryc > 0:
            try:
                result = fun()
                html = result[1]
                if result[0]:
                    break
            except Exception as e:
                print('请求出错')
            retryc -= 1
        return html

    return do_request


url = 'https://www.baidu.com'
session = requests.session()

@do_cycle_request
def temp_request():
    response = session.get(url)
    state_code = response.status_code
    if state_code < 300:
        return (True, response.content)
    else:
        return (False, 'null_html')

print(temp_request())