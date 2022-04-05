from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

tableClass = "table-products"
url = "https://steamdb.info/graph/"
CHROMEDRIVER_PATH = '/home/reaperfs/Development/webdriver_linux/chromedriver'
WINDOW_SIZE = '1920, 1080'

options = Options()
options.binary_location = "/usr/bin/brave"

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options= options)


def getHeader(table):
    tableHeader = table.find_element_by_css_selector("thead")
    tr = tableHeader.find_element_by_css_selector("tr")

    col = tr.find_elements_by_css_selector("th")
    headerList = [col[2].text, col[3].text, col[4].text, col[5].text]

    return headerList

def getBody(table):
    gameList = []

    tableBody = table.find_element_by_css_selector("tbody")
    for row in tableBody.find_elements_by_css_selector("tr"):
        elems = row.find_elements_by_css_selector("td")
        gameList.append([elems[2].text, elems[3].text, elems[4].text, elems[5].text])

    return gameList


def main():
    gameList = []
    headerList = []

    driver.get("https://steamdb.info/graph/")

    time.sleep(2)

    table = driver.find_element_by_class_name(tableClass)

    headerList = getHeader(table)
    gameList = getBody(table)

    df = pd.DataFrame(gameList, columns=headerList)

    df.to_csv("Top Steam Games.csv")

    driver.close()


if __name__ == "__main__":
    main()
