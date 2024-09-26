import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
alert_win = driver.switch_to.alert
alert_win.send_keys("Hello World!")
# print(alert_win.text)         # print the alert text
# alert_win.accept()            # Close alert window by using "OK" key
# alert_win.dismiss()           # Close alert window by using "CANCEL" key


time.sleep(5)
driver.quit()