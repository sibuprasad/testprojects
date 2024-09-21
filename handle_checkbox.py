import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10,poll_frequency=2)

checkboxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@id, 'day')]")
# print(len(checkboxes))

# Select all the checkboxes
# for i in checkboxes:
#     i.click()
#     print(i.get_attribute('id'))
# time.sleep(5)

# for i in range(0,len(checkboxes),2):
#     checkboxes[i].click()
#     print(checkboxes[i].get_attribute('id'))

# Select last 3 checkboxes
l = checkboxes[-3:]
for i in l:
    i.click()
    print(i.get_attribute('id'))

# Select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()
#         print(checkboxes[i].get_attribute('id'))

# Clearing all check boxes
for i in checkboxes:
    if i.is_selected():
        i.click()

driver.quit()