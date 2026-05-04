

import time
from itertools import dropwhile

from pyexpat.errors import messages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
#driver.get("http://localhost:3000/login")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

print(driver.title)
print(driver.current_url)



driver.find_element(By.ID, "autosuggest").send_keys("ind")

time.sleep(2)