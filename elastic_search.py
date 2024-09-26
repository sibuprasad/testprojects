import requests as request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver,10, poll_frequency=2)
driver.get("http://www.google.com/")
driver.maximize_window()

inputbox = driver.find_element(By.XPATH,'//*[@class="gLFyf"]')
inputbox.send_keys("narendra")

es = driver.find_element(By.XPATH,'//*[@id="Zrbbw"]/div[1]/span')
# print(es.tag_name)

driver.quit()