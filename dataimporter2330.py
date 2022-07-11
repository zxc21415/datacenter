


import os
import django,time
import pandas as pd
import twstock


# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Company,StockInfo


#抓台積電(2330)/台泥(1101)/亞泥(1102)/聯電(2303)/台達電子(2308)/長榮(2603)  資料
company_code = ["1101","1102","2303","2308","2603"]
#for com_code in company_code:
tsmc = twstock.Stock("2330")

#抓2022年1-6月/一年一年抓/每次隔30秒
for i in range(1,13):
    time.sleep(3)
    data = tsmc.fetch(2020,i)

    df = pd.DataFrame(data)
    
    dateinfo= list(df['date'])
    openinfo=list(df['open'])
    closeinfo=list(df['close'])
    transinfo=list(df['transaction'])
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
            pass
    print("第",i,"筆資料載入中")
    time.sleep(15)
    #print("換公司")
print("OK")
