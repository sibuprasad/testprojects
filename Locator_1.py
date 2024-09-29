import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(5)

act_data = driver.title
exp_data = "OrangeHRM"

if act_data == exp_data:
    print("Login Successful")
else:
    print("Login Failed")

driver.close()