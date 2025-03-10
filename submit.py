#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers

# 请注意替换APP_ID、APP_KEY
APP_ID = '3032715967'
APP_KEY = 'SiQeIoEmcMXHxILW'
URI = '/api/v1/task_submit'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'


def submit(prompt_text, prompt_type, APP_ID='3032715967', APP_KEY='SiQeIoEmcMXHxILW', METHOD='POST',
           URI='/api/v1/task_submit', DOMAIN='api-ai.vivo.com.cn'):

    if prompt_type == 1:
        style = '897c280803be513fa947f914508f3134'  # 日漫
    elif prompt_type == 2:
        style = '85ae2641576f5c409b273e0f490f15c0'  # 动漫
    elif prompt_type == 3:
        style = '85062a504de85d719df43f268199c308'  # 写实，实测完全不写实，是漫画风格
    elif prompt_type == 4:
        style = 'b3aacd62d38c5dbfb3f3491c00ba62f0'  # 绯红烈焰？其实就是以红色调为主
    else:  # 这里正确的输入是0，使用else是为了防止报错
        style = '55c682d5eeca50d4806fd1cba3628781'  # defualt，这个才是真正的写实风格

    params = {}
    data = {
        'height': 512,
        'width': 512,
        'prompt': prompt_text,
        'styleConfig': style
    }

    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    url = 'http://{}{}'.format(DOMAIN, URI)
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        print(response.status_code, response.text)




