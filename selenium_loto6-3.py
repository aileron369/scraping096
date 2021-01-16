from time import sleep
import pandas as pd
import datetime

#-------------------------------------------------------------------------------------------------csv読み込み
df = pd.read_csv('D:\D-VSCode\loto6_2021-01-16.csv').values.tolist()
#print(df)

loto_list = []

for list in df:
    loto_list.append(list[2:8])

jj = []
#print(loto_list)
for i in range(len(loto_list[0])):
    b = [x[i] for x in loto_list]  #<-----〇番目の数字を1個づつ取り出す
    jj.append(b)#<----------------------------〇番目ごとに配列[]にまとめる！！

#ループで表示するだけ
for i in range(len(jj)):
    print('--------------------'+str(i)+'個目-------------------')

    print(jj[i])  #<----------------それぞれ処理する（新しい配列に入れない）
    



#1/17できた！！


