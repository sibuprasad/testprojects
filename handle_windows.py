import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

try:
    # start = time.time()
    data = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class="wikipedia-search-input"]')))
    data.send_keys("selenium")
    data.submit()

    # Manual way
    # wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[@class="wikipedia-search-results"]//a)[1]'))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[@class="wikipedia-search-results"]//a)[2]'))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[@class="wikipedia-search-results"]//a)[3]'))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[@class="wikipedia-search-results"]//a)[4]'))).click()
    # wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[@class="wikipedia-search-results"]//a)[5]'))).click()

    # Using Looping
    path = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@class="wikipedia-search-results"]//a')))
    for i in path:
        i.click()
    wh = driver.window_handles
    for i in wh[1:]:
        driver.switch_to.window(i)
        print(driver.title)
        # if driver.title == "Selenium dioxide - Wikipedia":
        #     driver.close()

    # end = time.time()
    # print(end - start)

finally:
    None
    # driver.quit()