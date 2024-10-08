import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=2)
# driver.get("https://practice-automation.com/iframes/")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

try:
    # driver.switch_to.frame("bottom-iframe")
    # data = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Projects')))
    # data.click()
    # print(driver.find_element(By.XPATH,'//h3[text() = "Simple and concise"]').text)
    # time.sleep(2)

    # driver.switch_to.default_content()   # Switch back to the main frame
    # # driver.switch_to.parent_frame()      # Switch back to Parent frame if nested frame is available

    # driver.switch_to.frame("top-iframe")
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text() = "Docs"]'))).click()
    # header = wait.until(EC.element_to_be_clickable((By.XPATH,'//h2[@id="introduction"]')))
    # print(header.text)
    # time.sleep(2)

    start = time.time()
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text() = "Iframe with in an Iframe"]'))).click()
    outer = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
    driver.switch_to.frame(outer)
    inner = driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
    driver.switch_to.frame(inner)
    data = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/section/div/div/div/input')))
    data.send_keys('sibu')
    # time.sleep(2)
    data.clear()
    # time.sleep(2)
    driver.switch_to.parent_frame()
    driver.switch_to.frame(inner)
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/section/div/div/div/input'))).send_keys("jay sri ram")
    # time.sleep(5)
    end = time.time()
    print(end-start)

finally:
    driver.quit()