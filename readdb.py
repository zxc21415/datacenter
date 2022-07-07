# 寫獨立得程式來存取資料庫

import os
import django


# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import News






news_list = News.objects.all()



# Paginator 分頁器需要兩個引數
from django.core.paginator import Paginator
paginator = Paginator(news_list, 25)
# 資料總數
print('count', paginator.count)
# 總頁數
print('num_pages', paginator.num_pages)
# 頁碼的列表
print("page_range", paginator.page_range)
page1 = paginator.page(1)
print("page1", page1.object_list)
# print(news_list[:10])