from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ダウンロードしたChromedriverのPATHを教える(Windowsは'r'を頭に記述)
chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver'

options = Options() #Optionsモジュールを使う呪い
options.add_argument('--incognito')  #シークレットモードを使う
driver = webdriver.Chrome(executable_path=chrome_path, options=options) 


#driverでurlにアクセスする----------------------------------------------------------------------
url = 'https://www.binance.com/en/markets'
#url = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/loto6/index.html?year=2020&month=10'
#urlがChromeで開く
driver.get(url)
#requests.get(url)=>BeautifulSoupではない！

sleep(3)


#loto6にアクセスして、キーワード入力、閉じるところまで--------------------------------------
ps = driver.find_elements_by_tag_name('div')
sleep(2)

driver.quit()

for p in ps:
    print(p.text)







