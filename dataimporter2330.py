# 專門寫來轉資料的(從SQ3->MYSQL)


import os
import django,datetime
import pandas as pd
import twstock


# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Company,StockInfo


#抓台積電資料
tsmc = twstock.Stock("2330")

#抓2022年1-5月/一年一年抓/每次隔1分鐘

data = tsmc.fetch(2022,6)

df = pd.DataFrame(data)
dateinfo= list(df.date)
openinfo=list(df.open)
closeinfo=list(df.close)
transinfo=list(df.transaction)
alldata=zip(dateinfo,openinfo,closeinfo,transinfo)


tsmc_company = Company.objects.get(code="2330")
for d in alldata:
    #存進去
    try:
        rec = StockInfo(
            company= tsmc_company,
            dateinfo = d[0],
            open_price = d[1],
            close_price=d[2],
            volume=d[3]
        )
        rec.save()
    except Exception as e:
        print(e)