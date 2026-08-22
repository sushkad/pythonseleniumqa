import time
#from html.entities import name

from selenium import webdriver
from selenium.webdriver.common import options, alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractice/")

driver.find_elements(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)






