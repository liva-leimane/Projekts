import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.myavis.lv/lv/ilgtermina-auto-noma?period=&sort=asc" # atver vietni
driver.get(url)
time.sleep(2)

#sameklē "cookies" pogu un uzspiež accept
cookies_button = driver.find_element(By.XPATH, '//*[@id="cookieConsentForm"]/div[2]/div[4]/div/div/button')
time.sleep(2)
cookies_button.click()

degvielas_input = input("dīzelis, benzīns, elektroauto vai hibrīds: ")
degvielas = [degviela.strip() for degviela in degvielas_input.split(',')]#  vērtības tiek atdalītas ar komatu

degvielas_izvēle = {
    "elektroauto": "Elektroauto",
    "benzīns": "Benzīns",
    "dīzelis": "Dīzelis",
    "hibrīds": "Hibrīds"
}
