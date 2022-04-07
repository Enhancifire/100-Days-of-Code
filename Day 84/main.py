from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import json

with open("keys.json", "r") as f:
    data = json.load(f)


CHROMEDRIVER_PATH = '/home/reaperfs/Development/webdriver_linux/chromedriver'
WINDOW_SIZE = '1920, 1080'

options = Options()
options.binary_location = "/usr/bin/brave"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options= options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

print(driver.title)
time.sleep(2)

nameId = "username"
passId = "password"
buttonId = "btn__primary--large"

email = driver.find_element_by_id(nameId)
passw = driver.find_element_by_id(passId)
button = driver.find_element_by_class_name(buttonId)

email.send_keys(data["email"])
passw.send_keys(data["pass"])
button.click()



driver.close()
