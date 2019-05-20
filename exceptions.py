# coding=utf-8

"""define some exception"""


class MethodError(Exception):
    

    def __str__(self):
        return 'wrong Method, only accept get post'


class IsProxyError(Exception):
    

    def __str__(self):
        return 'wrong Proxy express, only accept yes/no'

class isSessionError(Exception):
    

    def __str__(self):
        return 'wrong Session express, on accept yes/no'


