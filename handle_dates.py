import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency = 2)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

inner_frame = driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]')
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

# # Example: 1    Using send key provide date 
# driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("10/10/2022")       # mm/dd/year

# # Example: 2    Using automation test script select date, month & year
month = "August"
year = "2023"
date = "30"

while True:
    mon = driver.find_element(By.XPATH,'//*[@class="ui-datepicker-month"]').text
    yr = driver.find_element(By.XPATH,'//*[@class="ui-datepicker-year"]').text
    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH,'//a[@title="Next"]').click()
        driver.find_element(By.XPATH,'//a[@title="Prev"]').click()

# # Date picker
dt = driver.find_elements(By.XPATH,'//*[@class="ui-datepicker-calendar"]//a')
for i in dt:
    if i.text == date:
        i.click()
        time.sleep(5)
        break        

driver.quit()