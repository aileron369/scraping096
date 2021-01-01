from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ダウンロードしたChromedriverのPATHを教える(Windowsは'r'を頭に記述)
chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver.exe'

options = Options() #Optionsモジュールを使う呪い
options.add_argument('--incognito')  #シークレットモードを使う
driver = webdriver.Chrome(executable_path=chrome_path, options=options) 


#driverでurlにアクセスする----------------------------------------------------------------------
url = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/loto6/index.html?year=2020&month=10'
driver.get(url)

#loto6にアクセスして、キーワード入力、閉じるところまで--------------------------------------
#td = driver.find_elements_by_tag_name('td')

class_names = 'js-lottery-number-pc'

td = driver.find_elements_by_xpath("//td[@class='alnCenter extension']")
sleep(3)
print('sleep(3)')

for t in td:
    print(t.text)
    sleep(1)
    print('sleep(1)')

driver.close()
driver.quit()
#ここまで可能
print('driver.quit')

#Driver閉じてから、処理を置くとNG->「 Failed to establish a new connection: [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。」








