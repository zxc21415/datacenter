from django.shortcuts import render
import random
from mysite.models import News
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
    #前面ID是欄位名稱
    item = News.objects.get(id=id)

    return render(requests,"show.html",locals())


