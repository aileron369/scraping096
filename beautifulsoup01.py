import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
res = requests.get(url)

soup = BeautifulSoup(res.text)


print('----------------------------------------------')
for ff in soup.find_all('h2'):
    print(ff.text) 



