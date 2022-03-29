from ssl import Options
from xml.dom.minidom import Element
from click import option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
PATH = Service("C:\chromedriver_win32\chromedriver.exe")


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=cookies")
driver=webdriver.Chrome(options=options,executable_path=os.getcwd())
driver = webdriver.Chrome(service=PATH)
driver.get("https://www.google.com/?hl=id")
search = driver.find_element_by_name("q")
search.send_keys("halu")
search.send_keys(Keys.RETURN)
link = driver.find_element_by_link_text("Gambar")
link.click()
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Video"))
    )
    element.click()
    
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,"q"))
    )
    element.clear()
    element.send_keys("ganteng")
    element.send_keys(Keys.RETURN)
except:
    driver.quit()