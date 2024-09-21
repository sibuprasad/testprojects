import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

#Using tag & id
# driver.find_element(By.CSS_SELECTOR,"#inputtext _55r1 _6luy").send_keys("sibu")

#Using tag & class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abcd")

#Using tag & attribute
# driver.find_element(By.CSS_SELECTOR,'input[data-testid="royal_email"]').send_keys("sibu prasad")

#Using tag, class & attribute (tag.class[attribute = value])
# driver.find_element(By.CSS_SELECTOR,'input.inputtext[aria-label="Password"]').send_keys("sibu987654")

# data = driver.find_elements(By.CSS_SELECTOR,'.inputtext')
# print(len(data))

# driver.quit()