import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # Example: 1
# service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver, 10, poll_frequency = 2)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()

# # Task: 1 -->  Count No of Rows & Columns
# noOfColumn = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]/th'))
# noOfRow = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[position() >1 and position() <= 7]'))
# print(noOfColumn,noOfRow)

# # Task: 2 -->  Read Specific Rows & Columns
# spRowData = driver.find_element(By.XPATH,'//table[@name="BookTable"]//tr[2]//td[2]')
# print(spRowData.text)

# # Task: 3 -->  Read all Rows & Column data
# noOfColumn = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]/th'))
# noOfRow = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[position() >1 and position() <= 7]'))
# for i in range(2,noOfRow+2):
#     for j in range(1,noOfColumn+1):
#         rows = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td["+str(j)+"]").text
#         print(rows,end="    ")
#     print()

# # Task: 4 -->  Read data based on conditions (List book name based on author name)
# noOfColumn = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[1]/th'))
# noOfRow = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr[position() >1 and position() <= 7]'))
# for i in range(2,noOfRow+2):
#     for j in range(1,noOfColumn+1):
#         author = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td["+str(j)+"]").text
#         if author == "Amit":
#             bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[1]").text
#             print(author,bookname)

# Example: 2
service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency = 2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="username"]'))).send_keys("Admin")
wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@name="password"]'))).send_keys("admin123")
wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text() = "Admin"]'))).click()
time.sleep(2)
noOfColumn = len(driver.find_elements(By.XPATH,'(//*[@class="oxd-table-row oxd-table-row--with-border"])[1]/div'))
noOfRow = len(driver.find_elements(By.XPATH,'//*[@class="oxd-table-body"]/div'))

for i in range(1,noOfRow+1):
    for j in range(1,noOfColumn+1):
        role = driver.find_element(By.XPATH,"//*[@class='oxd-table-body']/div["+str(i)+"]/div/div["+str(j)+"]").text
        if role == "ESS":
            emp_name = driver.find_element(By.XPATH,"//*[@class='oxd-table-body']/div["+str(i)+"]/div/div[4]").text
            print(role,":",emp_name)

driver.quit()