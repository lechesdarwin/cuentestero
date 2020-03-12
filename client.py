# -*- coding: utf-8 -*-

import pickle
import requests
import concurrent.futures
import sys

outdata = sys.argv[2]
inurl = sys.argv[1]
print("Entrada",inurl)
print("Salida",outdata)

data = []
URLS = []
#URLS = ['http://www.foxnews.com/',
#        'http://www.cnn.com/',
#        'http://europe.wsj.com/',
#        'http://www.bbc.co.uk/',
#        'http://some-made-up-domain.com/']
#
with open(inurl,"rb") as f:
    URLS = list(pickle.load(f))
    

h = {"Connection":"keep-alive"}
#URLS = URLS[20:]
# Retrieve a single page and report the URL and contents
def download(url:str):
    resp = requests.post("http://127.0.0.1:8888/",json={"url":url},headers=h)
    if resp.status_code == 200:
        print(url," Ok")
        data.append(resp)
        return resp
    else:
        print("error in ???")
        print(url)
        return "fail"


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
# Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(download, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            future.result()
            
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print(f'{url} page is {True} bytes')

print("Voy a escribir !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
with open(outdata,"wb") as f:
    pickle.dump(data,f)

#

#try:
#    for url in URLS:
#        r = requests.post("http://127.0.0.1:5555/",json={"url":url})
#        if r.status_code == 200:
#            data.append(r)
#        r.close()
#except Exception :
#    print("BOOOM una ")
#finally:
#    print("Voy a escribir !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#    with open("data.pkl","wb") as f:
#        pickle.dump(data,f)
#
