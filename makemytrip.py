import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://makemytrip.com/?srsltid=AfmBOoqKxe-DGTxfsiMsL94LhuAg5t6s31fiU0XtpEwqvwiW3Y79xuB9")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,'//*[@class="commonModal__close"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'(//*[@class="lbl_input appendBottom10"])[3]').click()
time.sleep(5)
driver.find_element(By.XPATH,'(//*[@class="dateInnerCell"])[42]').click()
time.sleep(5)
print(driver.title)
driver.close()