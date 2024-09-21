from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'C:\Users\sibup\Downloads\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
radio_count = len(radio_buttons)  # Correct usage of len() on a list of elements

print(f'Number of radio buttons: {radio_count}')
driver.quit()
