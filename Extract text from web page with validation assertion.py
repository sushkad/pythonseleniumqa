import time
from itertools import dropwhile

from pyexpat.errors import messages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
#driver.get("http://localhost:3000/login")
driver.get("https://rahulshettyacademy.com/client/")

print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter your email address']").send_keys("sushant@gmail.com")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Admin@1234")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Admin@1234")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").send_keys("Admin@1234")

