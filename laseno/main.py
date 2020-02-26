import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mobile_emulation = {"deviceMetrics": {"width": 425, "height": 550, "pixelRatio": 3.0}, "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
driver = webdriver.Chrome(executable_path=os.getenv("WEBDRIVER"),chrome_options=chrome_options)
driver.get('https://www.facebook.com/')
try:
    body = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.TAG_NAME,"body"))
    body.send_keys(Keys.CONTROL,Keys.SHIFT,"i")
except TimeoutException:
    pass

in_email = driver.find_element_by_id("m_login_email")
in_email.send_keys(os.getenv("USER_FB"))
in_pass = driver.find_element_by_id("m_login_password")
in_pass.send_keys(os.getenv("PASS_FB"))
btn = driver.find_element_by_name("login")
btn.click()
time.sleep(2)
btn = driver.find_element_by_css_selector("div._2pis")
btn.click()
time.sleep(3)
driver.find_element_by_tag_name("body").click()