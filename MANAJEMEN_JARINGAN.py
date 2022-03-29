from csv import DictReader
from logging import root
from re import T
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time
import schedule
PATH = Service("C:\chromedriver_win32\chromedriver.exe")

print("Welcome to absen otomatis")
print("Silahkan masukkan username dan password")
driver = webdriver.Chrome(service=PATH)
def absen():
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
    try:
        masuk = driver.find_element_by_xpath(
            "//div[@class='main-container']//div[2]//div[1]//div[3]//div[1]//a[1]").click()
        absen = driver.find_element_by_xpath("//button[@type='submit']").click()
        komentar = driver.find_element_by_xpath("//textarea[@placeholder='Berikan Komentar Anda Terhadap Pengajar Dosen']")
        komentar.send_keys("Selalu semangat")
        kirimkomen = driver.find_element_by_class_name("icon-send1").click()
        driver.quit()
    except:
        messagebox.showinfo("Absem", "Absen belum di buka")

# schedule.every().monday.at("11:05").do(absen)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
absen()