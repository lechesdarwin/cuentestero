# -*- coding: utf-8 -*-

import os
import re
import json
from flask import Flask
from flask import request
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# import psycopg2
from laseno.down import down
from laseno.u import down_img

folder = os.getenv("IMAGE")


def save_image(url):

    down_img(url, folder)


def funcname(self, parameter_list):
    raise NotImplementedError
# s = Serializer("token",expires_in=2)


app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    data = request.json
    data = down(data["url"])
    regex = r"([\w-]+\.(?:jpg|jpeg|svg|jpx|png|gif|webp|webp|cr2|x-canon-cr2|tif|tiff|bmp|jxr|vnd.ms-photo|psd|vnd.adobe.photoshop|ico|x-icon|heic))"
    img_url = []
    for im in data["img"]:
        m = re.search(regex, im)
        name = m.group(1)
        print(im)
        img_url.append("img/{}".format(name))
        #save_image(im)
    data["img"] = img_url
    res = json.dumps(data, ensure_ascii=False).encode('utf8')
    return res.decode()


app.run(port=5555)
