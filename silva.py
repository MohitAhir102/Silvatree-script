from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_service = Service('/Users/ztlab142/Downloads/chromedriver_mac64\ \(1\)/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

driver.get("https://sandbox.silvatree.co/")
driver.maximize_window()
time.sleep(20)

driver.find_element(By.XPATH,'//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]').click()
time.sleep(20)
time.sleep(20)