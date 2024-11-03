import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\Users\sibup\Downloads\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/List_of_national_flags_of_sovereign_states")

driver.maximize_window() # Maximize window size

# # 1. Scroll down page by pixe 
# driver.execute_script("window.scrollBy (0,5000)","")

# # 2. Scroll down page till element is visible 
# flag = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[81]/td[1]/figure/a/img')
# driver.execute_script("arguments[0].scrollIntoView();",flag)

# # 3. Scroll down page till the end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

"""
#1. Scroll down page by pixel 
#driver.execute_script("window.scrollBy(0,3086)", "") 
#value=driver.execute_script("return window.pageYOffset;") 
#print("Number of pixels moved:", value) #3800 

#2. Scroll down page till the element is visible 
#flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India"]") 
#driver.execute_script("arguments[0].scrollIntoView();",flag) 
#value=driver.execute_script("return window.pageYOffset;") 
#print("Number of pixels moved:", value) #5038.3330078125 

#3.scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") 
value=driver.execute_script("return window.pageYOffset;") 
print("Number of pixels moved:", value) #5990.8330078125

#4.scroll down page from end to start
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)") 
value=driver.execute_script("return window.pageYOffset;") 
print("Number of pixels moved:", value)
"""

time.sleep(5)