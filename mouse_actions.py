import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r'C:\Users\sibup\Downloads\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

element = driver.find_element(By.XPATH,'//*[@id="openwindow"]')
time.sleep(2)
actions = ActionChains(driver)
time.sleep(2)
actions.context_click(element).perform()
time.sleep(2)

driver.quit()