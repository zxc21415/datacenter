import json,requests,time
import os
import django

# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Company,StockInfo

#https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220711&stockNo=2303&_=1657527181297
url="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220{}01&stockNo={}"
#感興趣公司
company_code = ['2344','2337']
for com_code in company_code:
    for d in range(2,8):
    #開始請求(大範圍時測試時要加這段近來)
        time.sleep(3)
        get_url = url.format(d,com_code)
        get_data = requests.get(get_url)
        #print(get_url)
        time.sleep(3)
        get_data_text=get_data.text
        #print(type(get_data_text))
        get_data_json = json.loads(get_data.text)
        for all_data in get_data_json["data"]:
        #print(all_data[0]) 
        #print(type(all_data))
        #print('日期:',all_data[0],'開盤價:',all_data[3],'收盤價:',all_data[6],'成交筆數:',all_data[8])
            dateinfo_catch = (all_data[0].strip()).replace("111","2022").replace("/","-")
            #print(dateinfo_catch)
            openinfo_catch = float(all_data[3])
            closeinfo_catch = float(all_data[6])
            volume_catch=int(all_data[8].replace(",",""))
            #print('日期:',dateinfo_catch,'開盤價:',openinfo_catch,'收盤價:',closeinfo_catch,'成交筆數:',volume_catch)
            #載入資料庫寫法
            try:
                c = Company.objects.get(code=com_code)
                rec = StockInfo(company=c, dateinfo=dateinfo_catch, open_price=openinfo_catch, close_price=closeinfo_catch, volume = volume_catch)
                rec.save()
                print(com_code,"  ",d,"  月份載入完畢")
            except Exception as e:
                print(e)
        time.sleep(3)
print("OK")