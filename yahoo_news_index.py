import requests
from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/'

res = requests.get(url)
soup = BeautifulSoup(res.content) # 'html.parser'
index = soup.find('ul', 'topicsList_main')
listText = index.getText()

print(listText)

#動きません
#AttributeError: 'NoneType' object has no attribute 'getText -> AttributeError： 'NoneType'オブジェクトに属性 'getText'がありませ#

#-> https://teratail.com/questions/78472



