from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ダウンロードしたChromedriverのPATHを教える(Windowsは'r'を頭に記述)
chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver.exe'

options = Options() #Optionsモジュールを使う呪い
options.add_argument('--incognito')  #シークレットモードを使う
driver = webdriver.Chrome(executable_path=chrome_path, options=options) 

#driverでurlにアクセスする----------------------------------------------------------------------
url = 'https://www.mizuhobank.co.jp/retail/takarakuji/loto/loto6/index.html?year=2020&month=11'
driver.get(url)

#loto6にアクセスして、キーワード入力、閉じるところまで--------------------------------------

#Xpathで複数要素の指定ができる
helds = driver.find_elements_by_xpath("//th[@class='alnCenter bgf7f7f7 js-lottery-issue-pc']") #回数
sleep(3)
date = driver.find_elements_by_xpath("//td[@class='alnCenter js-lottery-date-pc']") #日付
sleep(3)
numbers = driver.find_elements_by_xpath("//td[@class='alnCenter extension']") #数字
sleep(3)


#print(number)には配列で、メモリ番地が乗っている----------------------------
#取り出してtextにせいや---＞
print('開催回数' + str(len(helds))) #9個ある
print('開催日数' + str(len(date))) #9個ある
print('数字総数' + str(len(numbers)))  #54個ある

held_list=[]
date_list = []
number_list = []
master_list=[]

#date日付からtextを取り出してheldsリストに入れる----------------------------------------------------------------------------
for held in helds:
    held_list.append(held.text)
#-->print(held_list)

#date日付からtextを取り出してdateリストに入れる----------------------------------------------------------------------------
for day in date:
    date_list.append(day.text)
#-->print(date_list)

#number配列メモリ番地からtextを取り出してnumberリストに入れる--------------------6個づつ---------------------------------------
for number in numbers:
    number_list.append(number.text)

#開始位置を指定
n = 0
#分割する変数の個数を指定
s = 6

#s個づつリストを分割する。
for i in number_list:
    master_list.append(number_list[n:n+s:1])  #<--配列にappendしてしまう（丸ごと）
    n += s #<-6回ループ
                    
    if n >= len(number_list):  #<-カウント数が配列の長さを超えたらループ終了
        break

#-----------------------------------------------------------配列頭に日付を追加
for i,day in enumerate(date_list):
    master_list[i].insert(0,day)

#-----------------------------------------------------------配列頭に回数を追加
for i,held in enumerate(held_list):
    master_list[i].insert(0,held)

print(master_list) 


#クローズ------------------------------------------------------------------------
driver.close()
driver.quit()
#ここまで可能
print('処理終了')


#-----------------------------------------------------------------------------ここからcsvに出力






#（注意）Driver閉じてから、処理を置くとNG->「 Failed to establish a new connection: [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。」

