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

#Xpathで複数要素の指定ができる
helds = driver.find_elements_by_xpath("//th[@class='alnCenter bgf7f7f7 js-lottery-issue-pc']") #回数
sleep(3)
date = driver.find_elements_by_xpath("//td[@class='alnCenter js-lottery-date-pc']") #日付
sleep(3)
number = driver.find_elements_by_xpath("//td[@class='alnCenter extension']") #数字
sleep(3)


#print(number)には配列で、メモリ番地が乗っている----------------------------
#取り出してtextにせいや---＞
print('開催回数' + str(len(helds))) #9個ある
print('開催日数' + str(len(date))) #9個ある
print('数字総数' + str(len(number)))  #54個ある

held_list=[]
date_list = []
dict_list = []

#date日付からtextを取り出してリストに入れる----------------------------------------------------------------------------
for held in helds:
    held_list.append(held.text)

print(held_list)

#date日付からtextを取り出してリストに入れる----------------------------------------------------------------------------
for day in date:
    date_list.append(day.text)

print(date_list)

#number配列メモリ番地からtextを取り出す---len(number)=54個----------------------6個づつ---------------------------------------
for element in number:
    dict_list.append(element.text)

#開始位置を指定
n = 0
#分割する変数の個数を指定
s = 6

#変数名カウント（ループ回数）
count=1

#s個づつリストを分割する。
for i in dict_list:
    locals()['name' + str(n + 1)] = dict_list[n: n + s :1]
    print('name' + str(count))
    print(dict_list[n: n + s :1])
    count += 1
    n += s
    
    #カウント数が配列の長さを超えたらループ終了
    if n >= len(dict_list):
        count=1
        break

print('dict_list総数' + str(len(dict_list)))
#print(dict_list)

#クローズ------------------------------------------------------------------------
driver.close()
driver.quit()
#ここまで可能
print('処理終了')


#（注意）Driver閉じてから、処理を置くとNG->「 Failed to establish a new connection: [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。」

