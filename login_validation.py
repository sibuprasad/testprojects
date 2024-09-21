import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(r'C:\Users\sibup\Downloads\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

collect_username = (driver.find_element(By.XPATH,'//*[@id="login_credentials"]').text).split("\n")
password_collect = (driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div[2]').text).split("\n")

username = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[1]/input")
password = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/input")

for i in range(1,len(collect_username)):
    for j in range(1,len(password_collect)):
        time.sleep(2)
        username.send_keys(collect_username[i])
        time.sleep(2)
        password.send_keys(password_collect[j])
        time.sleep(2)
        login = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)
    fetch_text = driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').text
    print(fetch_text)
    # addto_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    # time.sleep(5)
    # check_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').click()
    # time.sleep(5)
    break
driver.quit()