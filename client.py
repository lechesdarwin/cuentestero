# -*- coding: utf-8 -*-

import pickle
import requests


urls = []
data = []
with open("url.pkl","rb") as f:
    urls = pickle.load(f)

try:
    for url in urls:
        r = requests.post("http://127.0.0.1:5555/",json={"url":url})
        if r.status_code == 200:
            data.append(r)
        r.close()
except Exception :
    pass
finally:
    with open("data.pkl","wb") as f:
        pickle.dump(data,f)
