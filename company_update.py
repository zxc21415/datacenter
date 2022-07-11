#------------
#  新增公司
#------------
url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
import requests
from bs4 import BeautifulSoup

# Django設定
import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
from mysite.models import CompanyType,Company

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
            # 從網頁中解析出公司的資料
            code,name,ct=cells[0].text.split("　")[0],cells[0].text.split("　")[1],cells[4].text
            print(code,name,ct) #代碼 名字 類別
            #去除重複種類(取得公司類別在資料表中的紀錄)
            # 先去CompanyType撈資料
            company_type = CompanyType.objects.get(name=ct.strip())
            # 去公司看看有沒有新增過了
            rec = Company.objects.filter(name=name.strip())
            if len(rec) == 0:
                #沒有找到重複的，才要把公司資訊存進去
                rec = Company(ct=company_type,code = code.strip(),name=name.strip())
                rec.save()
        except:
            pass