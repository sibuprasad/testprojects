import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,30, poll_frequency=2)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html/")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

# # Mouse move then click
# wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@name="username"]'))).send_keys("admin")
# wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@name="password"]'))).send_keys("admin123")
# wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@type="submit"]'))).click()
# admin = wait.until(EC.visibility_of_element_located((By.XPATH,'(//*[text() = "Admin"])[1]'))).click()
# usrmgt = wait.until(EC.element_to_be_clickable((By.XPATH,'(//*[@class="oxd-topbar-body"]//li)[1]'))).click()
# user = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="oxd-topbar-body-nav-tab-link"]'))).click()
# action = ActionChains(driver)
# action.move_to_element(usrmgt).move_to_element(user).click().perform()

# # Mouse double click
# dc = driver.find_element(By.XPATH,'//*[@ondblclick="myFunction1()"]')
# action = ActionChains(driver)
# action.double_click(dc).perform()

# # Mouse Right click
# rclickpath = driver.find_element(By.XPATH,'')
# action = ActionChains(driver)
# action.context_click(rclickpath).perform()

# # Mouse drag & drop
# source = driver.find_element(By.XPATH,'//*[@id="box6"]')
# destination = driver.find_element(By.XPATH,'//*[@id = "box106"]')
# action = ActionChains(driver)
# action.drag_and_drop(source,destination).perform()

# time.sleep(5)

driver.quit()