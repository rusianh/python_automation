import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

#TODO Init chrome
service = Service(excutable_path="chromedriver")
driver = webdriver.Chrome(service=service)
#TODO
driver.get("https://google.com")  # truy cap link
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with Tim" + Keys.ENTER)

#todo Fine link text
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()


time.sleep(10)
driver.quit()