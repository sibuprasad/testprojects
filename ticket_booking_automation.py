import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency = 2)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

start = time.time()

ticket = driver.find_element(By.XPATH,'//*[@id="product_549"]')
ticket.click()
driver.find_element(By.XPATH,'//*[@id="travname"]').send_keys("Sibu Prasad")
driver.find_element(By.XPATH,'//*[@id="travlastname"]').send_keys("Nanda")
driver.find_element(By.XPATH,'//*[@id="dob"]').click()
month = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-month"]'))
month.select_by_visible_text("Jun")
year = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-year"]'))
year.select_by_visible_text("1997")
date = driver.find_elements(By.XPATH,'//*[@class="ui-datepicker-calendar"]//a')
for i in date:
    if i.text == "3":
        i.click()
        break

driver.find_element(By.XPATH,'//*[@id="sex_1"]').click()
driver.find_element(By.XPATH,'//*[@id="traveltype_1"]').click()
driver.find_element(By.XPATH,'//*[@id="fromcity"]').send_keys("Bangalore")
driver.find_element(By.XPATH,'//*[@id="tocity"]').send_keys("Bhubaneswar")

driver.find_element(By.XPATH,'//*[@id="departon"]').click()
month_d = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-month"]'))
month_d.select_by_visible_text("Nov")
year_d = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-year"]'))
year_d.select_by_visible_text("2024")
date_d = driver.find_elements(By.XPATH,'//*[@class="ui-datepicker-calendar"]//a')
for i in date_d:
    if i.text == "9":
        i.click()
        break

driver.find_element(By.XPATH,'(//*[@aria-haspopup="true"])[6]').click()
driver.find_element(By.XPATH,'//*[@class="select2-search__field"]').send_keys("Visa application")
visa = ActionChains(driver)
visa.send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH,'//*[@id="appoinmentdate"]').click()
month_a = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-month"]'))
month_a.select_by_visible_text("Nov")
year_a = Select(driver.find_element(By.XPATH,'//*[@class="ui-datepicker-year"]'))
year_a.select_by_visible_text("2024")
date_a = driver.find_elements(By.XPATH,'//*[@class="ui-datepicker-calendar"]//a')
for i in date_a:
    if i.text == "7":
        i.click()
        break

driver.find_element(By.XPATH,'//*[@id="deliverymethod_1"]').click()
driver.find_element(By.XPATH,'//*[@id="billname"]').send_keys("Delloit")
driver.find_element(By.XPATH,'//*[@id="billing_phone"]').send_keys("1234567890")
driver.find_element(By.XPATH,'//*[@id="billing_email"]').send_keys("erik@gmail.com")

driver.find_element(By.XPATH,'(//*[@class="select2-selection select2-selection--single"])[7]').click()
driver.find_element(By.XPATH,'//*[@class="select2-search__field"]').send_keys("India")
country = ActionChains(driver)
country.send_keys(Keys.ENTER).perform()

driver.find_element(By.ID,"billing_address_1").send_keys("Bangalore")
driver.find_element(By.XPATH,'//*[@id="billing_city"]').send_keys("Bnagalore")

driver.find_element(By.XPATH,'//*[@id="select2-billing_state-container"]').click()
driver.find_element(By.XPATH,'//*[@class="select2-search__field"]').send_keys("Karnataka")
action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH,'//*[@id="billing_postcode"]').send_keys("789456")

driver.find_element(By.XPATH,'//*[@id="place_order"]').click()

# time.sleep(5)

end = time.time()
print(end - start)

driver.quit()