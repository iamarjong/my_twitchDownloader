'''
此為個人 myvscode 裡的 "研究娜珉.py" 的一個函式
會這樣取檔名是因為那時真的一邊 "練英聽" 一邊想流程
''' 


def version3(帳號='shishichuchu', 
瀏覽器已開=False         ,
手動讀m3u8='', 外部命令路徑=r'c:\Users\User\Desktop\外部命令.txt',  # 建立外部命令.txt 要用的
資料夾 = r'c:\Users\User\Downloads'): 

    path_to_browsermobproxy = r'c:\Users\User\Desktop\爬蟲物件包\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin'+'\\'
    K=[]  # 防止 K在宣告前就使用
    s=''
    結束函式 = False 
    file_sizes=[]

    last = ''   #最後一個影片的編號

    第幾圈 = 0 
    不是200次數 = 0 
    重取m3u8次數 = 0 


    
    while True: 

        if 結束函式 ==True : 
            break 

        第幾圈+=1 


        '''  
        第一步： 把 Chrome 打開
        '''

        if 瀏覽器已開==False and 手動讀m3u8=='': 
            server0 = Server(path_to_browsermobproxy 
                            + "browsermob-proxy.bat", options={'port': 8090})    # 改 8091 會出事？ 
            print("server0→ ",end="")
            server0.start() 
            print("server0→ ",end="")

            proxy0 = server0.create_proxy(params={"trustAllServers": "true"}) 
            print("proxy0→ ",end="")
            options0 = webdriver.ChromeOptions() 
            print("options0→ ",end="")
            #options0.add_argument('headless')               # 瀏覽器不要顯示
            #print("options0→ ",end="")
            options0.add_argument("--ignore-certificate-errors") 
            print("options0→ ",end="")
            options0.add_argument("--proxy-server={0}".format(proxy0.proxy)) 
            print("options0→ ",end="")
            driver0 = webdriver.Chrome(options=options0)    
            print("driver0→ ",end="")
            proxy0.new_har("twitch.tv") 
            print("proxy0→ Chrome啟動完成→  ",end="")

            瀏覽器已開 = True 




        '''  
        第二步： (1) 載入網頁並取得 .har 
                (2) 讓瀏覽器一邊涼快去
        '''


        if 手動讀m3u8=='':

            driver0.set_page_load_timeout(40)
            try: 
                driver0.get("https://www.twitch.tv/"+帳號) 
            except: 
                ...  # 狀態 = 讀取失敗

            print("twitch 網頁啟動完成。 " ,end="")


            K=[]
            ddd=proxy0.har 
            for i in range(len(ddd['log']['entries'])):
                if ddd['log']['entries'][i]['request']['url'].find(帳號)==40:  #[40] 
                    K.append(i)

            if len(K)==1:
                第一個m3u8=ddd['log']['entries'][K[0]]['request']['url']
            elif len(K)>1: 
                print("K=",K)
                #for i in K: 
                    #print(ddd['log']['entries'][i]['request']['url'])
                第一個m3u8=ddd['log']['entries'][K[-1]]['request']['url']

            else: 
                print("K=[]")
            

            print('\n第一個m3u8=' ,第一個m3u8)

            driver0.get('data:,') 

        else: 

            第一個m3u8=手動讀m3u8  
            print('\n第一個m3u8=' ,第一個m3u8)
            手動讀m3u8=''
  
            # 要判斷手動讀 m3u8 是否真是個 m3u8 
            # 否則要設置要 m3u8 的機制


        '''   
        第三步： 取得裡面m3u8的 ts 網址串
        '''
        M=100
        for i in range(M): 
            print('開始抓取內部m3u8的 ts 網址串 (l)。')
            r=requests.get(第一個m3u8 ,stream=True) 
            if r.status_code==200: 
                不是200次數 = 0 
                重取m3u8次數 = 0
                print("抓取成功，正在解析。")
                l=r.text.split('\n') 
                print("l[4]=" , l[4] ) 
                r=requests.get( l[4] ,stream=True)  
                l=r.text.split('\n') 
                #l[10].find('2023')    # 找到 76
                #片段名=l[10][76:100].replace(':','-')
                if len(l)>10: 
                    print("l[11]=",l[11])     # l[10] 不知道幹什麼的
                else: 
                    print("l[11] 找不到東西，進新的一圈。") 
                    print() 
                    continue 

                print()
            else:
                print("r.status_code 是",r.status_code,", 不是 200。") 
                不是200次數+=1 
                if 不是200次數 == 3-重取m3u8次數: 
                    不是200次數=0 
                    print('已連續', 3-重取m3u8次數, '次不是200，重新要一個新的第一個m3u8。 ')
                    重取m3u8次數+=1 
                    print() 
                    if 重取m3u8次數 == 3:
                        return '瀏覽器故障'
                    break 
                print() 
                 
                # 處理 version 3 小壞的情況: 
                # 即，這個瀏覽器要重開的問題。 







                # ----------------
                # 要做這段
                # ----------------

                if len(K)>1: 
                    第一個m3u8=ddd['log']['entries'][K[-1]]['request']['url']
                
                continue

            '''  
            第四步： 下載 ts 檔串
            '''

            print("( i=",i,") 開始截取 l 的 ts 檔，已完成:", end="\n")
            temp=[]
            number=0
            for i in range(11, len(l) ,3):
                if len(l[i])>43:
                    if l[i][38]==':'  and l[i][36:44]>last:
                        subanswer=[]
                        subanswer.append(l[i][36:44])   # 要比對用的，不能改掉冒號
                        subanswer.append(l[i+2]) 
                        if int(l[i][42:44]) - number !=2 and  int(l[i][42:44]) - number !=-58: 
                            subanswer.append('不連號')
                        number = int(l[i][42:44]) 
                        temp.append(subanswer)
                else: 
                    print('l[',i,'] 長度 < 44， l[',i,']=',l[i])
            '''  
            temp 的例子: 
            temp = [  ['13:20:55', 2秒影片的網址]
                    ,['13:20:57', ----網址]
                    ,[ '13:30:00', -----網址, '不連號' ]
                ]
            '''
            
            if temp!=[]:
                last = temp[-1][0] 
            for i in temp:
                r=requests.get(i[1],stream=True)
                f=open(資料夾 + '\\'+ i[0].replace(':','-') +'.ts','ab')
                f.write(r.content)
                f.close() 
                file_sizes.append(len(r.content))
                print(i[0], ', ',end="")

                # 檢查是否要廣告警告
                if len(file_sizes)>3: 
                    if file_sizes[-1]!=file_sizes[-4]:
                        file_sizes=file_sizes[-3:]
                    else: 
                        print('file_sizes = ',file_sizes,',', end="")
                if len(file_sizes)>5:

                    # 檢查標準差  
                    
                    print('file_sizes = ',file_sizes,'，廣告警告。')
                    return '廣告警告'
                
                print() 

            print()
            if i!=M-1: 
                time.sleep(5)
            #print(l[i]) 


            # 檢查外部令命
            f=open(外部命令路徑, 'r')
            s = f.readline()
            f.close() 
            f=open( 外部命令路徑  ,'w')
            f.close() 
            if s=='結束':
                結束函式 = True 
                break 

            # elif s == 'm3u8' or 'm3u8\n' 
    
    return '完成'

