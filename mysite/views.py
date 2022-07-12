from ast import keyword
from plotly.offline import plot
import plotly.graph_objs as go
from django.shortcuts import render
import random
from mysite.models import CompanyType, News,Company,StockInfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


#定義一個finc叫index
#給網頁用的要求第一個參數要request
def index(request):
    if request.method=="POST":
        #針對內文查詢
        #查詢進
        keyword = request.POST.get("keyword")
        get_news = News.objects.filter(content__contains=keyword)
    else:
        #首頁進
        get_news = News.objects.all()
    count= len(get_news)
    url = "/"
    name = "DyAF"
    #用哪個HTML顯示
    # LOCALS() =>打包此函示所有東西

    #很醜要用串列生程式比較好看、會重複號碼
    # lotto = []
    # for i in range(6):
    #     num = random.randint(1,49)
    #     lotto.append(num)

    # 串列生程式
    #lotto = [lotto.append(random.randint(1,49)) for i in range(6)]

    # # 會重複號碼 = > shuffle 洗牌
    # lotto = [i for i in range(1,50)] #先照順序排列
    # random.shuffle(lotto)            #再利用 洗牌 打亂順序
    # lotto = lotto[:6]                #取出前六個

    # 從DB撈資料，存到變數才可以放去首頁
    # News.objects.all().order_by('欄位') 可以換順序
    #get_news = News.objects.all()


## 此行肯定要修
    # current_page = News.objects.get(p)
    # paginator = Paginator(get_news, 25)
    
    # try:
    #     page = paginator.page(current_page)
    #     # has_next              是否有下一頁
    #     # next_page_number      下一頁頁碼
    #     # has_previous          是否有上一頁
    #     # previous_page_number  上一頁頁碼
    #     # object_list           分頁之後的資料列表
    #     # number                當前頁
    #     # paginator             paginator物件
    # except PageNotAnInteger:
    #     page = paginator.page(1)
    # except EmptyPage:
    #     page = paginator.page(paginator.num_pages)
    



    return render(request,"index.html",locals())

def lotto(requests):
    url = "lotto"
    lotto = [i for i in range(1,50)] #先照順序排列
    random.shuffle(lotto)            #再利用 洗牌 打亂順序
    lotto = lotto[:6]                #取出前六個
    for i in range(6) :
        if lotto[i]<10:
            lotto[i] = "0"+str(lotto[i])

    return render(requests,"lotto.html",locals())


def show(requests,id):
    #前面ID是欄位名稱，後面是參數
    item = News.objects.get(id=id)

    return render(requests,"show.html",locals())

def page(requests,pg):
    get_news = News.objects.all()
    current_page = pg
    paginator = Paginator(get_news, 25)
    
    try:
        page = paginator.page(current_page)
        # has_next              是否有下一頁
        # next_page_number      下一頁頁碼
        # has_previous          是否有上一頁
        # previous_page_number  上一頁頁碼
        # object_list           分頁之後的資料列表
        # number                當前頁
        # paginator             paginator物件
        page_list = page.object_list
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(requests,"page.html",locals())


def stock(requests):
    url = "stock"
    ct = CompanyType.objects.all()
    return render(requests,"stock.html",locals())

def company(requests,id):
    #前面ID是欄位名稱，後面是網址參數
    ct = CompanyType.objects.get(id=id)
    #這個ct再傳入Company去尋找相同的資料內容
    companies = Company.objects.filter(ct=ct)
    return render(requests,"company.html",locals())

#預設參數id=1
def stockinfo(request,id=1):
    #找出是從按鈕近還是表單進
    if request.method=="POST": #表單進
        comp = request.POST.get("comp") #SELECT NAME
        print(comp)
        company = Company.objects.get(id = comp)
    else:  #如果不是使用表單轉來這個網頁，就直接使用參數id來找出公司
        company = Company.objects.get(id = id)

    #此處ID要等於台積電ID
    #company = Company.objects.get(id=id)
    #靠ID去stockinfo抓資料(表格用)
    data = StockInfo.objects.filter(company=company).order_by('dateinfo')[:50]
    last50 = data[:50]  #資料表用的
    #畫圖用的1
    prices = [d.open_price for d in data]
    prices2 = [d.close_price for d in data]
    volumes=[ (d.volume/1000) for d in data ]  #以千為當單位
    dates = [d.dateinfo for d in data]
    #原先
    #plot_div = plot([go.Scatter(x=dates,y=prices,mode='lines')],output_type="div" )
    #改為兩條
    plot_div = plot([go.Scatter(x=dates,y=prices,mode='lines'),go.Scatter(x=dates,y=prices2,mode='lines'),go.Bar(x=dates,y=volumes)],output_type="div" )
    return render(request,"stockinfo.html",locals())

def chart(request):
    #處理關鍵字資料
    keywords=""
    #表單進
    if request.method=="POST":
        keywords = request.POST.get("keywords")
    if keywords=="":
        #預設值:
        keywords="雲科,北科,高科"
    keywords = keywords.split(",")
    data = list()
    for keyword in keywords:
        data.append(News.objects.filter(content__contains=keyword.strip()).count())
        
    return render(request,"chart.html",locals())

    