之前写的那版http api不好用

重写一遍

写好顺手为止

发现需要的功能 requests的作者都帮我想到了

我直接二次封装就行了

### 使用

    from requestApi import HttpApi
    api = HttpApi()
    html = api.send_args_get_html(
        url=xxxxx,
        headers=xxxxxx,
        params=xxxxxx,
        payloads=xxxxxx,
        cookies=xxxxxx,
        method='get/post',
        isProxy='yes/no',
        isSession='yes/no',
        code='gbk/utf-8/xxx'
    )