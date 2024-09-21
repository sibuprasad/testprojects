import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
# time.sleep(5)

# try:
#     driver.find_element(By.XPATH, '(//*[@class = "_27h2j1"])[1]').click()
#     # driver.find_element(By.PARTIAL_LINK_TEXT,"Men's Top").click()
#     driver.find_element(By.LINK_TEXT, "Men's Top Wear").click()
#     driver.find_element(By.LINK_TEXT, "Men's T-Shirts").click()
#     time.sleep(5)
# except Exception as e:
#     print(driver.title)
#     print("Error raised",e)
# finally:
    # driver.quit()

# Total no of sliders by the class name
sliders = driver.find_elements(By.XPATH,'//*[@class = "css-175oi2r r-cdmcib r-1xbve24 r-1cy1rn1 r-8hc5te"]')

# Total no of links or anchor tags
links = driver.find_elements(By.TAG_NAME,'a')
print(len(sliders))
print(len(links))

driver.quit()