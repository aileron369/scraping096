import requests
from bs4 import BeautifulSoup
#import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver'
options = Options()
options.add_argument('--incongnito')
driver = webdriver.Chrome(executable_path=chrome_path,options=options)


url = 'https://www.python.org/'
driver.get(url)

sleep(5)

driver.quit()


