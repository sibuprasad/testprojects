import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# driver.get('https://snapdeal.com/')
driver.get('https://www.amazon.in/')
driver.maximize_window()
time.sleep(5)

# Count no of anchor tags in the footer section
# print(len(driver.find_elements(By.XPATH,'//*[@class="navLeftFooter nav-sprite-v1"]//a')))
# print(driver.find_elements(By.XPATH,'//*[@class="navLeftFooter nav-sprite-v1"]//a')[-1].text)
driver.find_element(By.XPATH,'//*[text() = "Sports shoes"]').click()

data = driver.find_element(By.XPATH,'(//*[@class="a-icon a-icon-checkbox"])[4]')
print(data.get_attribute('class'))
print("data: ", data.text)


# driver.back()   #snapdeal
# time.sleep(5)
# driver.forward()    #amazon
# time.sleep(5)
# driver.refresh()
# time.sleep(5)

# Browser commands
# driver.close()
# driver.quit()

