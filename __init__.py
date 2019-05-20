# coding=utf-8

"""
    author: wangjiawei
    version: 2.0

    笔者重构一个版本的请求库
    我自己的轻框架非得scrapy？

    在之前的版本里，遇到以下的问题
    1. 执行时间长
    2. session.proxies里有代理，但是请求仍旧从本地发出
    3. 自动判断网页编码出错
    4. 逻辑复杂
    5. 日志看不懂
    6. 引用不便捷
    
    update:
    05-16: todo: 如何引入时候，将日志也如项目当前的路径
"""

__all__ = ['httpApi']

from .requestApi import httpApi