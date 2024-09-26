import requests as request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver,10, poll_frequency=2)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

brokenlinks = driver.find_elements(By.XPATH,'//a')
broken_links_count = 0
valid_links_count = 0
broken_links = []
valid_link = []

for i in brokenlinks:
    url = i.get_attribute('href')
    try:
        res = request.head(url)
    except:
        None
    if res.status_code >= 400:
        broken_links.append(url)
        broken_links_count += 1
    else:
        valid_link.append(url)
        valid_links_count += 1

print("Broken Links Count: ", broken_links_count)
print("Valid Links Count: ", valid_links_count)

driver.quit()