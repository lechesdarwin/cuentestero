# -*- coding: utf-8 -*-
import os
import re
import time
from bs4 import BeautifulSoup
import requests
import httpx

def rrss(test_str):
    regex = r"(@(\w+))"
    subst = "<a rel='nofolow norefer' href=\"https://twitter.com/\\2\" target=\"_blank\">\\1</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    regex = r"(#(\w+))"
    subst = "<a href=\"https://twitter.com/hashtag/\\2\" target=\"_blank\">\\1</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    regex = r"[^\'\"](https?:\/\/((www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6})\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"
    subst = " <a href=\"\\1\" target=\"_blank\" rel='nofollow norefer'>\\2</a>"
    result = re.sub(regex, subst, test_str, 0, re.IGNORECASE | re.UNICODE)
    if result:
        test_str = result
    return test_str

def href(name):
    return "-".join(name.split(" ")).lower()

def id_tuit_text_plain(text,lis):
    regex = r"https:\/\/twitter.com/\w+/status/(\d+)"
    m = re.search(regex, text)
    re.search
    if m:
        lis.append(m.group(1))


def down_e(url,pined=False):
    h = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36"}
    r = requests.get(url,headers=h)
    bs = BeautifulSoup(r.content.decode("utf8"), "html.parser")
    content = bs.find("main",{"class":"content"})
    title = content.find("h1", {"class":"entry-title", "itemprop":"headline"}).get_text()
    tuit = content.find_all("a",{"href":re.compile(r"https:\/\/t\.co\/(\w+)")})
    img = content.find_all("img",limit=4)
    img_link = []
    tuit_links = []
    link_tuit = []
    if tuit:
        for a in tuit:
            tuit_links.append(a.attrs["href"])
        tmp = [requests.get(link).url for link in tuit_links]
        for i in tmp:
            id_tuit_text_plain(i, link_tuit)
    if img:
        for i in img:
            img_link.append(i.attrs["src"])
    date = content.find("time", {"class":"entry-time"}).get_text()
    categorias = [i.text for i in content.find("span",{"class":"entry-categories"}).find_all("a")]
    external = content.find_all("iframe")
    contento = []
    external_link = []
    if external:
        try:
            for i in external:
                external_link.append(i.attrs["src"])
        except Exception:
            print("Error into exernals links")
    
    
    
    # for i in content.find_all("p"):
    #     if len(i.text) > 6 and i.em == None :
    #         contento.append(i.text
    for p in bs.find_all("p"):
        if p.attrs.get("class") == "entry-meta":
            continue
        elif p.img:
            continue
        elif p.get_text().startswith("Fuente") and p.a:
            continue
        elif p.em:
            pass
        elif p.get_text().startswith("Copyright") and p.a:
            break
        else:
            contento.append(p.get_text())
    
    print("flush")
    contento = [rrss(cnt) for cnt in contento]
    contento = "*#*".join(contento)
    contento = "{} *$* {}".format(title, contento)
    return dict(content=contento, categorias=categorias, date=date, img=img_link, external=external_link, link=href(title), tuit=link_tuit, pined=pined)