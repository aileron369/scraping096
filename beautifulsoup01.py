import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.python.org/'
res = requests.get(url)

soup = BeautifulSoup(res.text)

sleep(1)

print('----------------------------------------------')
for ff in soup.find_all('h2'):
    print(ff.text) 





