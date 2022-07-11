#自己抓，自己解析 HTML
url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
import requests
from bs4 import BeautifulSoup

# Django設定
import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
from mysite.models import CompanyType

html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")
rows = soup.find_all("tr")


#用迴圈取出全部
for i,row in enumerate(rows):  #rows 一堆<tr>
    if i>=2:
        try:
            cells=row.find_all("td")  # 從一堆<tr>  找到<td>
            if cells[0].text[0] == "0": 
                break
            code,name,ct=cells[0].text.split("　")[0],cells[0].text.split("　")[1],cells[4].text
            print(code,name,ct) #代碼 名字 類別
            #去除重複種類
            #讀取CompanyType裡面的物件，名子叫做=ct.strip() [每一筆的類別]，存進去rec當中
            #如果rec有找到任何一筆，表示已經存過了，就不存這筆了
            rec = CompanyType.objects.filter(name=ct.strip())
            if len(rec) == 0:
                #沒有找到重複的，就存進去
                rec = CompanyType(name=ct.strip())
                rec.save()
        except:
            pass