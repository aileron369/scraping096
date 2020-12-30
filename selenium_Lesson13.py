from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ダウンロードしたChromedriverのPATHを教える(Windowsは'r'を頭に記述)
chrome_path = r'D:\D-VSCode\chromedriver_win32\chromedriver'

options = Options() #Optionsモジュールを使う呪い
options.add_argument('--incognito')  #シークレットモードを使う
driver = webdriver.Chrome(executable_path=chrome_path, options=options) 


#driverでurlにアクセスする----------------------------------------------------------------------
url = 'https://search.yahoo.co.jp/image'
#urlがChromeで開く
driver.get(url)
#requests.get(url)=>BeautifulSoupではない！

sleep(3)


#yahooにアクセスして、検索欄にキーワード入力、閉じるところまで--------------------------------------
keyword = 'プログラミング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(keyword)
search_box.submit()

sleep(3)

#WEB画面をスクロールする(Javascriptを記述)-------------------------------------------------------
height = 1000
while height < 3000:
    driver.execute_script('window.scrollTo(0,{});'.format(height))
    height += 100
    print(height)
    sleep(1)

#画像のclass名を選択する
elements = driver.find_elements_by_class_name('sw-Thumbnail')

#Class名からurlを取得する
for i,element in emunerate(elements, start=1):
    element.find






driver.quit()


