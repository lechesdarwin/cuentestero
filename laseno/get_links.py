import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pickle

def href(name):
    return "-".join(name.split(" ")).lower()


def get_links(url, rango=[0, 700], ciestas=[0.3, 0.1],ele="a",de={"class":"entry-title-link"}):
    mobile_emulation = {"deviceMetrics": {"width": 425, "height": 550, "pixelRatio": 3.0}, "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(executable_path=os.getenv("WEBDRIVER"), chrome_options=chrome_options)
    driver.get(url)
    time.sleep(1.5)
    for _ in range(rango[0], rango[1]):
        time.sleep(ciestas[0])
        driver.execute_script("window.scrollBy(0,160)")
    time.sleep(ciestas[1])

    # time.sleep(3)
    html = driver.page_source
    driver.close()
    # print(html)
    bs = BeautifulSoup(html, "html.parser")
    a = bs.find_all(ele, de)
    print(a)
    urls = [u.attrs["href"] for u in a]
    with open("url.pkl", "wb") as f:
        pickle.dump(urls, f)
print("calledewde")
get_links("http://eju.tv/")