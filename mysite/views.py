from django.shortcuts import render
import random
from mysite.models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


#定義一個finc叫index
#給網頁用的要求第一個參數要request
def index(requests):
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
    get_news = News.objects.all()


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
    



    return render(requests,"index.html",locals())

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


