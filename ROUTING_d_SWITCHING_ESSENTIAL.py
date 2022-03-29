from csv import DictReader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = Service("C:\chromedriver_win32\chromedriver.exe")

print("Welcome to absen otomatis")
print("Silahkan masukkan username dan password")
driver = webdriver.Chrome(service=PATH)
driver.get("http://elearning.bsi.ac.id/login")
email = driver.find_element_by_name("username")
email.send_keys("17200693")
pw = driver.find_element_by_name("password")
pw.send_keys("@1ahKuwa09")
button = driver.find_element_by_tag_name("Button")
button.click()
jadwal = driver.find_element_by_id("pin-sidebar")
jadwal = driver.find_element_by_class_name("sidebar-dropdown")
jadwal.click()
jadwal0 = driver.find_element_by_xpath(
    "//a[normalize-space()='Jadwal Kuliah']")
jadwal0.click()
masuk = driver.find_element_by_xpath(
    "//div[@class='row gutters']//div[1]//div[1]//div[3]//div[1]//a[1]").click()
absen = driver.find_element_by_xpath("//button[@type='submit']").click()
komentar = driver.find_element_by_name("komentar")
komentar.send_keys("Selalu semangat")
kirimkomen = driver.find_element_by_class_name("icon-send1").click()
driver.quit()
