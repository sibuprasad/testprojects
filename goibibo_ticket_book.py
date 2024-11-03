import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency = 2)
driver.get("https://www.goibibo.com/")
driver.maximize_window()


try:
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@class="sc-jlZhew inxprl"]'))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class="sc-12foipm-70 fPPRk"]'))).click()

    # # Source City
    # driver.find_element(By.XPATH,'(//*[@class="sc-12foipm-2 eTBlJr fswFld "])[1]').click()
    # driver.find_element(By.XPATH,'//*[@type="text"]').send_keys("Bengaluru")
    # s_cities = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="autoSuggest-list"]//li//span[@class="autoCompleteTitle "]')))
    # for i in s_cities:
    #     if "Bengal" in i.text:
    #         i.click()
    #         break

    # # Destination City
    # driver.find_element(By.XPATH,'//*[@type="text"]').send_keys("Bhubaneswar")
    # d_cities = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="autoSuggest-list"]//li//span[@class="autoCompleteTitle "]')))
    # for j in d_cities:
    #     if "Bhubane" in j.text:
    #         j.click()
    #         break

    # Date picker
    wait.until(EC.element_to_be_clickable((By.XPATH,'(//*[@class="sc-12foipm-2 eTBlJr fswFld "])[3]'))).click()
    
    while True:
        next_click = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class="DayPicker-NavButton DayPicker-NavButton--next"]')))
        dates = driver.find_elements(By.XPATH,'//*[@class="DayPicker-Months"]/div[1]/div[position() <=1 or position() >= 3]')

        found_data = False

        for month in dates:
            if "December 2024" in month.text:
                datepicker = driver.find_elements(By.XPATH,'//*[@class="DayPicker-Months"]/div[1]/div[3]/div/div')
                for day in datepicker:
                    if day.text == "12":
                        day.click()
                        found_data = True
                        break
                break
        if found_data:
            break 
        else:
            next_click.click()

    print(driver.find_element(By.XPATH,'(//*[@class="sc-12foipm-4 czGBLf fswWidgetTitle"])[1]').text)
    # time.sleep(2)
    # driver.find_element(By.XPATH,'(//*[@class="sc-12foipm-2 eTBlJr fswFld "])[5]').click()
    # driver.find_element(By.XPATH,'//*[@class="sc-12foipm-64 jkgFUQ"]').click()
    # driver.find_element(By.XPATH,'//*[@class="sc-12foipm-72 ezNmSh"]').click()
    time.sleep(2)

except Exception as e:
    print(e)

finally:
    driver.quit()