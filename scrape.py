from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

import requests
import json
import datetime

url = 'https://www.kemkes.go.id'
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
delay = 60  # seconds


try:
    myElem = WebDriverWait(browser, delay).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'covid-case-container')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
finally:
    indonesia_positif = browser.find_element_by_xpath(
        '//*[@id="vbMainLayer"]/div[6]/div/ul/li[5]/table/tbody/tr[1]/td[3]').text
    indonesia_sembuh = browser.find_element_by_xpath(
        '//*[@id="vbMainLayer"]/div[6]/div/ul/li[5]/table/tbody/tr[2]/td[3]').text
    indonesia_meninggal = browser.find_element_by_xpath(
        '//*[@id="vbMainLayer"]/div[6]/div/ul/li[5]/table/tbody/tr[3]/td[3]').text
    print("indonesia_positif: {}".format(indonesia_positif))
    print("indonesia_sembuh: {}".format(indonesia_sembuh))
    print("indonesia_meninggal: {}".format(indonesia_meninggal))

covid_data = {
    "Indonesia": {
        "Positif": int(indonesia_positif.replace(",", "")),
        "Sembuh": int(indonesia_sembuh.replace(",", "")),
        "Meninggal": int(indonesia_meninggal.replace(",", "")),
    },
    "Date Retrieved": str(datetime.datetime.now()),
    "Source": url,

}

print('covid_data: {}'.format(covid_data))

# Write to json file
with open('covid_data.json', 'w') as outfile:
    json.dump(covid_data, outfile)

browser.close()
