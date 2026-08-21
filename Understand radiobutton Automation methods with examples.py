import time

from selenium import webdriver
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)