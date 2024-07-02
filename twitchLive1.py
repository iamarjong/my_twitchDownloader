import argparse
parser = argparse.ArgumentParser()
parser.add_argument('twitch_account', type=str, help='實況主帳號')
args = parser.parse_args()
帳號=args.twitch_account

瀏覽器已開=False          
手動讀m3u8= '' 
開始的版本 = 2 # 原 3
廣告警告的策略 = 2

from selenium import webdriver 
from browsermobproxy import Server 
from selenium.webdriver.common.by import By
import sys,os
sys.path.append(r"C:\Users\User\Documents\myvscode\231102_myPackage")
sys.path.append(r"C:\Users\User\Documents\myvscode\231025 twitch")
from mine import * 
from 研究娜珉4 import *

time_factor=getTimeFactor()
專案名稱 = 實況主名單[帳號][0]+' '+ time_factor 
I數量=5  # 改完後就真的是數量了
I數量長度= len(str(I數量))
資料夾= r'c:\Users\User\Desktop\研究娜珉'+ '\\' + 就是要建立資料夾(   資料夾名=專案名稱 ,在哪建=r'c:\Users\User\Desktop\研究娜珉')
外部命令路徑 = r'c:\Users\User\Desktop\外部命令\外部命令 (' + 專案名稱 + ').txt'
f=open(外部命令路徑  ,'w')
f.close() 

#輸出設定資料
print("帳號→          ", 帳號) 
print("名字→          ", 實況主名單[帳號][0])
print("存儲的根資料夾→ " ,資料夾)
print()


# 設定 version 3 的資料夾
# 並執行 version 3
資料夾編號 = 0 
子資料夾= 資料夾 + '\\' + str(資料夾編號)
if not os.path.exists(子資料夾): 
    os.mkdir(子資料夾)  

次數 = 0 
while True: 

    狀態 = version3(帳號=帳號 ,  
                瀏覽器已開=瀏覽器已開,
                手動讀m3u8=手動讀m3u8, 
                外部命令路徑=外部命令路徑, 
                資料夾 = 子資料夾,
                )


    break 


print()
print()

手動讀m3u8 = ''

while 狀態 !='完成': 

    if 狀態 == '廣告警告':
        
        資料夾編號 +=1 
        子資料夾= 資料夾 + '\\' + str(資料夾編號)
        if not os.path.exists(子資料夾): 
            os.mkdir(子資料夾)  

        if 廣告警告的策略 ==2 : 
            
            狀態 = version2 (  帳號=帳號 ,  
                    瀏覽器已開=瀏覽器已開,
                    外部命令路徑=外部命令路徑, 
                    資料夾 = 子資料夾,
                    duration = 15*60

            )

            if 狀態=='OK': 

                資料夾編號 +=1 
                子資料夾= 資料夾 + '\\' + str(資料夾編號)
                if not os.path.exists(子資料夾): 
                    os.mkdir(子資料夾)  


                狀態 = version3(帳號=帳號 ,  
                    瀏覽器已開=瀏覽器已開,
                    手動讀m3u8=手動讀m3u8, 
                    外部命令路徑=外部命令路徑, 
                    資料夾 = 子資料夾,
                    )
            else :   # 其他狀態還沒建構
                ...

            
        elif 廣告警告的策略 == 1: 

            # 響起聲音
            driver1 = webdriver.Chrome()    
            driver1.get('https://youtu.be/PJiDJQMqoyQ')

            # 在 狀況回報.txt 中輸入出問題的那個
            f=open(r'c:\Users\User\Desktop\狀況回報.txt', 'a')
            f.write(專案名稱+' 出狀況了，應去填好 m3u8 檔。\n')
            f.close() 

            # 掛機
            _ =input('廣告警告的策略 == 1 , 應去填入 手動讀m3u8。')


            # 取得新的 m3u8 參數
            f=open(外部命令路徑,'r')
            s=f.readline() 
            f.close() 
            手動讀m3u8 = s 


            狀態 = version3(帳號=帳號 ,  
                瀏覽器已開=瀏覽器已開,
                手動讀m3u8=手動讀m3u8, 
                外部命令路徑=外部命令路徑, 
                資料夾 = 子資料夾,
                )

    elif 狀態 == '瀏覽器故障':
        狀態 = version3(帳號=帳號 ,  
                瀏覽器已開=瀏覽器已開,
                手動讀m3u8=手動讀m3u8, 
                外部命令路徑=外部命令路徑, 
                資料夾 = 子資料夾,
                )


print('結束。 ')
