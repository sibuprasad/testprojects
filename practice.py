"""
driver.current_window_handle # Current WindowsID
driver.window_handles        # List of WindowsID
driver.switch_to.window(WindowsID)
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency = 2)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# col_count = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]//th')
# row_count = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr [position() >1 and position() <= 7]')

# print(len(col_count),len(row_count))        # Count no of Rows & Columns
# col,row = [i.text for i in col_count], [i.text for i in row_count]
# print(col,row)                              # Print all Rows and Columns

# Print all Rows and Columns
# for i in range(2,len(row_count)+2):
#     for j in range(1,len(col_count)+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#         print(data,end="          ")
#     print()

# bookname_col_path = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr//td[1]')
# author_path = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr//td[2]')
# sub_path = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr//td[3]')
# price_path = driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr//td[4]')

# for i in range(2,len(row_count)+2):
#     author = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[2]").text
#     if author == "Amit":
#         subject = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[3]").text
#         price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[4]").text
#         print(author, subject, price)

driver.quit()