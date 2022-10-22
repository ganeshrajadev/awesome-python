#Get Fast.com results straight from your CLI

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
def cmdfast():
    os.environ['MOZ_HEADLESS'] = '1'
    url = "https://www.fast.com/"
    browser = webdriver.Firefox()

    browser.get(url)
    time.sleep(1)
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')

    soup.find_all("div")
    datadump = str(soup.find("div", {"id": "speed-value"})).split()[2]
    unitdump = str(soup.find("div", {"id": "speed-units"})).split()[2]
    d = datadump.split('>')[1].split('<')[0]
    u = unitdump.split('>')[1].split('<')[0]
    print(d,u)
    browser.quit()

cmdfast()
