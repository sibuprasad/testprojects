import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])

try:
    driver.get("https://makemytrip.com/")
    driver.maximize_window()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-cy="closeModal" and @class="commonModal__close"]'))).click()

    datepick = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@for="departure"]')))
    datepick.click()
    switchdate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@role="button" and @aria-label="Next Month"]')))

    for _ in range(12):
        switchdate.click()
        x = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="DayPicker-Caption" and @role="heading"]')))
        if x[0].text == "August 2025" or x[1].text == "August 2025":
            driver.find_element(By.XPATH, '(//*[@class="dateInnerCell"])[32]').click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '(//*[@class="blackText font20 code lineHeight36"])[1]')))
            break
    print(driver.find_element(By.XPATH, '(//*[@class="blackText font20 code lineHeight36"])[1]').text)

except Exception as e:
    print("Error message: ", e)

finally:
    driver.quit()