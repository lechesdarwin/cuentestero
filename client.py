# -*- coding: utf-8 -*-

import pickle
import requests
#import concurrent.futures


data = []
URLS = []
#URLS = ['http://www.foxnews.com/',
#        'http://www.cnn.com/',
#        'http://europe.wsj.com/',
#        'http://www.bbc.co.uk/',
#        'http://some-made-up-domain.com/']
#
with open("url.pkl","rb") as f:
    URLS = pickle.load(f)


# Retrieve a single page and report the URL and contents
def load_url(url):
    r = requests.post("http://127.0.0.1:5555/",json={"url":url})
    if r.status_code == 200:
        return r

# We can use a with statement to ensure threads are cleaned up promptly
#with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#    # Start the load operations and mark each future with its URL
#    future_to_url = {executor.submit(load_url, url): url for url in URLS}
#    for future in concurrent.futures.as_completed(future_to_url):
#        url = future_to_url[future]
#        try:
#            d = future.result()
#            data.append(d)
#        except Exception as exc:
#            print('%r generated an exception: %s' % (url, exc))
#        else:
#            print(f'{url} page is {d.status_code} bytes')
#

try:
    for url in URLS:
        r = requests.post("http://127.0.0.1:5555/",json={"url":url})
        if r.status_code == 200:
            data.append(r)
        r.close()
except Exception :
    print("BOOOM una ")
finally:
    print("Voy a escribir !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    with open("data.pkl","wb") as f:
        pickle.dump(data,f)
