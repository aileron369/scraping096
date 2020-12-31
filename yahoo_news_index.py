import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://shourinken123amakita.wordpress.com/'

res = requests.get(url)
soup = BeautifulSoup(res.content) 
index_news = soup.find_all('h2')
#listText = index.getText()
sleep(2)

for hh in index_news:
    print(hh.text)






#動きません
#AttributeError: 'NoneType' object has no attribute 'getText -> AttributeError： 'NoneType'オブジェクトに属性 'getText'がありませ#

#-> https://teratail.com/questions/78472



