#https://www.geeksforgeeks.org/scrape-table-from-website-using-python-selenium/
#https://selenium-python.readthedocs.io/navigating.html#popup-dialogs
#https://selenium-python.readthedocs.io/waits.html
#https://www.scrapingbee.com/blog/selenium-python/
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
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep

print('enter serial number')
serial_number = input()
part = input()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r'C:/Users/biven/mypythonscripts/chromedriver')

driver.get('https://partsurfer.hp.com/Search.aspx')

wait = WebDriverWait(driver, 10)

select = Select(driver.find_element_by_name(
    'ctl00$BodyContentPlaceHolder$ddlCountry'))
select.select_by_visible_text('United States')

element = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "// *[@id='onetrust-accept-btn-handler']"))).click()

#alert = driver.switch_to.alert

textElem = driver.find_element_by_name(
    "ctl00$BodyContentPlaceHolder$SearchText$TextBox1")
textElem.send_keys(serial_number)
textElem.submit()
searchElem = driver.find_element_by_xpath("//*[@id='ctl00_BodyContentPlaceHolder_SearchText_btnSubmit']").click()

sleep(2)

rows = 1+len(driver.find_element_by_xpath(
    "/ html/body/div[1]/form/div[3]/table[2]/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[4]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr"))#2
#original xpath rows
#/html/body/div[1]/form/div[3]/table[2]/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[4]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr[2]

# example cols /html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[2]/div/table/tbody/tr[1]/td[1]

# original xpath cols /html/body/div[1]/form/div[3]/table[2]/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[4]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]
cols = 2+len(driver.find_elements_by_xpath(
    "/ html/body/div[1]/form/div[3]/table[2]/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[4]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr[2]/td"))#3

print(rows)
print(cols)
print("Locators         "+"         Description")

for r in range(2, rows+1):
    for p in range(1, cols+1):
        value = driver.find_element_by_xpath(
        "/html/body/div[3]/form/div[3]/table[2]/tbody/tr/td/div/div/div[2]/table/tbody/tr[2]/td/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[4]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
        print(value, end='      ')
    print()

 #elementRows = driver.find_elements_by_xpath(
 #   )
#print(elementList)
#try:
#    cookies = WebDriverWait(driver, 15).until(
#        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
 #       )
#finally:
    #driver.quit()
    #.find_element_by_id('onetrust-accept-btn-handler').click()
    #print('nothing yet')
#except NoSuchElementException:
 #   print('dunno')


#def getHPpartNumber(productUrl):
#    res = requests.get(productUrl)
#    res.raise_for_status()
