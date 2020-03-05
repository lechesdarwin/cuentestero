import os
from flask import Flask, request
from laseno.u import down_img


app = Flask(__name__)
folder = os.getenv("IMAGE")


@app.route("/", methods=['POST'])
def save():
    js = request.json
    print(js)
    down_img(js["url"], folder)
    return "OK"


app.run(port=8888)
