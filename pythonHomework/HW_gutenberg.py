from bs4 import BeautifulSoup as bs
import requests as req
import re, os

# 取得書目列表
url = "https://www.gutenberg.org/browse/languages/zh" 

# 用 requests 的 get 方法把網頁抓下來
response = req.get(url) 

# 指定 lxml 作為解析器
soup = bs(response.text, "lxml") 

# 建立資料夾
folderPath = '古騰堡'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

# 建立 list 來放置連結
list_a = []
list_name = []
# 取得 a 的連結 
for a in soup.select('li.pgdbetext a'):
    if (re.search(r'[\u4E00-\u9FFF]',a.get_text())):
        list_a.append(re.search(r'\d{3,6}',a['href'])[0]) # 擷取書碼
        list_name.append(re.sub(r'[^\u4E00-\u9FFF]','',a.get_text())) # 取得書名

# 取得內文頁面連結
list_book = []
for b in list_a:
    list_book.append(f'https://www.gutenberg.org/files/{b}/{b}-0.txt')

for i in range (len(list_book)):
    print(list_name[i])
    print(list_book[i])

list_content = []
book = ''
# 非空白*2+中文字+非空白*2 
grex = r'[\S]{0,4}[\u4E00-\u9FFF]+[\S]*' 

# 走訪每一本書名&內容
for i in range (len(list_book)):
    book=''
    with open(f'./古騰堡/{list_name[i]}.txt', 'w', encoding='UTF-8') as f:
        res=req.get(list_book[i])
        # 改變文字編碼
        res.encoding = 'UTF-8'
        soup = bs(res.text, "lxml") 
# 寫入檔案
        for x in re.findall(grex, soup.text):
            # book += x
            f.write(f'{x}\n')
