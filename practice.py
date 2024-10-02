import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(3)

driver.quit()