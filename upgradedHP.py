from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import bs4
import requests
import webbrowser
import sys
import pyperclip
import pandas as pd
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
#8cg7222dcd
page = requests.get('https://partsurfer.hp.com/Search.aspx')
page.raise_for_status()

print('enter serial number')
serial_number = input()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/user/mypythonscripts/chromedriver')
driver.get('https://partsurfer.hp.com/Search.aspx')

wait = WebDriverWait(driver, 10)

select = Select(driver.find_element_by_name(
    'ctl00$BodyContentPlaceHolder$ddlCountry'))
select.select_by_visible_text('United States')

element = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "// *[@id='onetrust-accept-btn-handler']"))).click()

textElem = driver.find_element_by_name(
    "ctl00$BodyContentPlaceHolder$SearchText$TextBox1")
textElem.send_keys(serial_number)
textElem.submit()
searchElem = driver.find_element_by_xpath(
    "//*[@id='ctl00_BodyContentPlaceHolder_SearchText_btnSubmit']").click()

testUrl = driver.current_url
print(testUrl)
def get_all_tabs_of_player_page(URL=testUrl):
    driver = webdriver.Chrome()
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'html')
    driver.quit()
    tables = soup.find_all('table', {"class": ["table_sortable  tbl"]})
    tabs_dic = {}

    for table in tables:
        tab_name = table['id']

        tab_data = [[cell.text for cell in row.find_all(
            ["tr", "td"])] for row in table.find_all("tr")]
        df = pd.DataFrame(tab_data)
        df.columns = df.iloc[0, :]
        df.drop(index=0, inplace=True)

        tabs_dic[tab_name] = df

    return tabs_dic



dfs = pd.read_html(testUrl, match='Spare BOM (HP Orderable Product BOM)')
#8cg7222dcd
print(f'Total tables: {len(testUrl)}')

#https://towardsdatascience.com/scrape-tabular-data-with-python-b1dd1aeadfad
#https: // pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write
#https: // pbpython.com/pandas-html-table.html
#https://felleisen.org/matthias/HtDC/htdc.pdf
#https://www.selenium.dev/documentation/webdriver/browser_manipulation/
#https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
