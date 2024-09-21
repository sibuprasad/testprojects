import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/")
driver.maximize_window()

driver.implicitly_wait(10)
# It'll not wait for the expected time to complete, it'll handle synchronisation problems automatically
# It can only be mentioned once

searcbox = driver.find_element(By.ID,'APjFqb')
searcbox.send_keys("google pixel 9")
searcbox.submit()
driver.find_element(By.XPATH,'//*[text() = "Pixel 9 with Gemini & AI Photo Editing"]').click()

# time.sleep(5)
# Performance of the script is very poor, if any operation completed before the given time it'll still wait for the time to complete.
# If element is n't available in the expected time, exception may arise
