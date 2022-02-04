from selenium import webdriver
import selenium

chrome_driver_path = "E:\\Development\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path= chrome_driver_path)

url = "https://www.amazon.in/Kindle-10th-Gen/dp/B07FQ4Q7MB/"
driver.get(url)

elem = driver.find_element(".a-price-whole")
print(elem)

driver.quit()
