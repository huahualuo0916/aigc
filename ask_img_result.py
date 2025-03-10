#!/usr/bin/env python
# encoding: utf-8

import requests
import base64
import json
from auth_util import gen_sign_headers


APP_ID = '3032715967'
APP_KEY = 'SiQeIoEmcMXHxILW'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'GET'


def ask_img_result(task_id):
    params = {
        # 替换为提交作画任务时返回的task_id
        'task_id': task_id
    }
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)

    uri_params = ''
    for key, value in params.items():
        uri_params = uri_params + key + '=' + value + '&'
    uri_params = uri_params[:-1]

    url = 'http://{}{}?{}'.format(DOMAIN, URI, uri_params)
    # print('url:', url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        print(response.status_code, response.text)


# ask_img_result('31ccbb983034550fbbbb646ef353b9df')
