# -*- coding: utf-8 -*-
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from . import u


def href(name):
    return "-".join(name.split(" ")).lower()


def down(url, rango=[0, 11], ciestas=[0.2, 0.1], f=None, pined=False):
    mobile_emulation = {"deviceMetrics": {"width": 425, "height": 550, "pixelRatio": 3.0}, "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=os.getenv("WEBDRIVER"), chrome_options=chrome_options)
    driver.get(url)

    for _ in range(rango[0], rango[1]):
        time.sleep(ciestas[0])
        driver.execute_script("window.scrollBy(0,160)")
    time.sleep(ciestas[1])

    # time.sleep(3)
    html = driver.page_source
    driver.close()
    # print(html)
    bs = BeautifulSoup(html, "html.parser")

    cont = bs.find("div", {"class":"entry-content", "itemprop":"text"})
    tuit = []
    if bs.find_all("twitter-widget"):
        for tui in bs.find_all("twitter-widget"):
            tuit.append(int(tui.attrs["data-tweet-id"]))
    img = cont.find_all("img", limit=2)
    title = bs.find("h1", {"class":"entry-title", "itemprop":"headline"}).get_text()
    date = bs.find("time", {"class":"entry-time"}).get_text()
    categorias = [i.text for i in bs.find("span",{"class":"entry-categories"}).find_all("a")]
    content = []
    external = []
    for i in cont.find_all("p"):
        if len(i.text) > 6 and i.em == None :
            content.append(i.text)
        elif i.iframe:
            external.append(i.iframe)
    if f:
        f(bs)
    else:
        print("flush")
    if external:
        external = [ext.attrs["src"] for ext in external]
    if img:
        img = [im.attrs["src"] for im in img]
    content = [u.rrss(cnt) for cnt in content]
    content = "*#*".join(content)
    content = "{} *$* {}".format(title, content)
    return dict(content=content, categorias=categorias, date=date, img=img, external=external, link=href(title), tuit=tuit, pined=pined)
