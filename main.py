# 这是一个示例 Python 脚本。
import requests
import base64
import json
from auth_util import gen_sign_headers

from submit import submit
from get_img_id import get_img_id
from ask_img_result import ask_img_result
from text2img import text2img

APP_ID = '3032715967'
APP_KEY = 'SiQeIoEmcMXHxILW'
URI = '/api/v1/task_progress'
DOMAIN = 'api-ai.vivo.com.cn'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    img_url = text2img(text="男", type=0)
    print(img_url)
