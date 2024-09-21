import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r'C:\Users\sibup\Downloads\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

open_window_button = driver.find_element(By.XPATH, '//*[@id="openwindow"]')
open_window_button.click()

all_handles = driver.window_handles

driver.switch_to.window(all_handles[1])
driver.maximize_window()
course_link = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
course_link.click()

time.sleep(5)

driver.close()
# driver.switch_to.window(all_handles[0])
driver.quit()