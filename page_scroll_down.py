import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

service = Service(r'C:\Users\sibup\Downloads\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

#Using PageDown
# element = driver.find_element(By.XPATH,'//*[@id="openwindow"]')
# time.sleep(2)
# element.send_keys(Keys.PAGE_DOWN)
# time.sleep(2)

#Using ActionChains
# actions = ActionChains(driver)
# time.sleep(5)
# actions.move_to_element(element).perform()
# time.sleep(5)