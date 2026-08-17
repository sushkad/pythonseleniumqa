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

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(4)

countries = driver.find_element(By.CSS_SELECTOR, "li[class ='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break


print(driver.find_element(By.ID,"autosuggest")).__getattribute__("value")