from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r'C:\Users\sibup\Downloads\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')

serch_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("Selnium Webdriver")
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'))).click()

driver.implicitly_wait(5)

driver.quit()