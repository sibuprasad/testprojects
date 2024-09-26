import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

links = driver.find_elements(By.XPATH,'//a')
# print(len(links))

# Print all the links name
# for i in links:
#     print(i.text)



driver.quit()