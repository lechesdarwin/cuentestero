import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

mobile_emulation = {"deviceMetrics": {"width": 425, "height": 550, "pixelRatio": 3.0}, "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
driver = webdriver.Chrome(executable_path=os.getenv("WEBDRIVER"),chrome_options=chrome_options)
driver.get("http://eju.tv/2020/02/mira-como-anabel-tira-la-toalla-en-una-playa-colombiana/")
time.sleep(4)

for count in range(10, 100):
    time.sleep(0.2)
    driver.execute_script("window.scrollBy(0,100)")

driver.execute_script("window.scrollBy(0,0)")
time.sleep(0.2)

# time.sleep(3)
html = driver.page_source
driver.close()
# print(html)
bs = BeautifulSoup(html,"html.parser")

print(bs.find_all("div",{"class":"entry-content","itemprop":"text"}))

