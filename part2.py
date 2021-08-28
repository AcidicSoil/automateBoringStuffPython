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
from scrape_test import testUrl
from bs4 import BeautifulSoup
URL = testUrl
page = requests.get(URL)

print(page.text)
soup = BeautifulSoup(page.text, "html.parser")
stories = []

for td in soup.find_all('td', attrs={'class': 'RowStyle', 'class': 'AlternatingRowStyle'}):
    print(stories[0])


partRegex = re.compile(r'[a-z]')

print(partRegex.findall(
    stories[len(testUrl)]))
#use the link below like the mapit exercise and the last part will be sn
#https: // partsurfer.hp.com/Search.aspx?searchText = 8cg7222dcd
