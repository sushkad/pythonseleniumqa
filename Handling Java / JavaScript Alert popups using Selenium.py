import time
#from html.entities import name

from selenium import webdriver
from selenium.webdriver.common import options, alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

name ="sushant"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)

driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text

print(alertText)

assert name in alertText
alert.accept()



