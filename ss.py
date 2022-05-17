# Python program to demonstrate
# selenium

# import webdriver

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# create webdriver object
driver = webdriver.Chrome()

# enter keyword to search


# get geeksforgeeks.org
driver.get("https://www.amazon.in/")

# get element
#element = driver.find_element_by_xpath('//*[@id="gcse-search-input"]')

b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="twotabsearchtextbox"]')))

# print complete element
#print(element)

b.send_keys("mobile")


s = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-search-submit-button"]')))

s.click()




