from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

CHROMEDRIVER_PATH = '/home/reaperfs/Development/webdriver_linux/chromedriver'
WINDOW_SIZE = '1920, 1080'

options = Options()
options.binary_location = "/usr/bin/brave"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options= options)

driver.get("https://linkedin.com")

print(driver.title)
driver.close()
