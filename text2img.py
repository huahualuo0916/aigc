import requests
import base64
import json
from auth_util import gen_sign_headers
import time

from submit import submit
from get_img_id import get_img_id
from ask_img_result import ask_img_result


def text2img(text, type, wait_seconds=10):
    # print(text)
    response = submit(text, type)
    if type == 3:
        wait_seconds = 20

    if not get_img_id(response):
        return -1

    img_id = get_img_id(response)

    for i in range(0, wait_seconds):
        print("AI出图中，请耐心等待")
        time.sleep(1)
    result = ask_img_result(img_id)

    if not result['result']['finished']:
        # print(result)
        print("超时")
        return -1
    else:
        return result['result']['images_url']

