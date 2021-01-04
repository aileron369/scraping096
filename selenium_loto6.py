from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy

#ダウンロードしたChromedriverのPATHを教える(Windowsは'r'を頭に記述)
chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver.exe'

options = Options() #Optionsモジュールを使う呪い
options.add_argument('--incognito')  #シークレットモードを使う
driver = webdriver.Chrome(executable_path=chrome_path, options=options) 

#driverでurlにアクセスする----------------------------------------------------------------------
url = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/loto6/index.html?year=2020&month=10'
driver.get(url)

#loto6にアクセスして、キーワード入力、閉じるところまで--------------------------------------

#Xpathで複数要素の指定ができる
td = driver.find_elements_by_xpath("//td[@class='alnCenter extension']")
sleep(3)


#print('tdには配列で、メモリ番地が乗っている----------------------------')
#print(td)#取り出してtextにせいや---＞
print(len(td))#54個ある

dict_list = []


#td配列メモリ番地からtextを取り出す---len(td)=54個----------------------6個づつ---------------------------------------
for element in td:
    dict_list.append(element.text)

    #日付を入れたい----------------------------------------------------------------------------------
    #date = element.find_elements_by_xpath("//td[@class='alnCenter js-lottery-date-pc']")

#開始位置を指定
n = 0
#分割する変数の個数を指定
s = 6

#s個づつリストを分割する。
for i in dict_list:
    print(dict_list[n:n+s:1])
    n += s
    
    
    #カウント数が配列の長さを超えたらループ終了
    if n >= len(dict_list):
        break

print('dict_list総数' + str(len(dict_list)))
#print(dict_list)

#クローズ------------------------------------------------------------------------
driver.close()
driver.quit()
#ここまで可能
print('処理終了')


#（注意）Driver閉じてから、処理を置くとNG->「 Failed to establish a new connection: [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。」

