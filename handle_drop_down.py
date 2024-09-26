import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver,10, poll_frequency=2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drpd_ele = Select(driver.find_element(By.XPATH,'//*[@id="country"]'))
# drpd_ele.select_by_index(0)
# drpd_ele.select_by_visible_text("India")

drpd = drpd_ele.options
for i in range(len(drpd)):
    if drpd[i].text == "France":
        drpd[i].click()
        print(drpd[i].text)


# drpdown = driver.find_elements(By.XPATH,'//*[@id="country"]//option')
# for i in drpdown:
#     i.text == "India"
#     i.click()

time.sleep(2)
driver.quit()