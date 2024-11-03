# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

"""
driver.current_window_handle                # Current WindowsID
driver.window_handles                       # List of WindowsID
driver.switch_to.window(WindowsID)

driver.find_element().click()
driver.find_element().send_keys()           # Dynamic Drop down
visa = ActionChains(driver)
visa.send_keys(Keys.ENTER).perform()

driver.switch_to.frame(webelement / name / id)
driver.switch_to.default_content()          # Move back to intial/first outer frame
driver.switch_to.parent_frame()             # Move back to its parent frame

action = ActionChains(driver)                # Mouse left click action
action.move_to__element(webelement).click().perform()

action = ActionChains(driver)
action.double_click(webelement).perform()   # Double click on a button (mouse double click for a task to perform)

action = ActionChains(driver)
action.context_click(webelement).perform()  # Mouse right click action
"""

