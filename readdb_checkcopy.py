# 檢查有沒有重複

import os
from unicodedata import name
import django


# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import CompanyType




abc=CompanyType.objects.get(name="其他業").id
print(abc)
# news_list = StockInfo.objects.filter(dateinfo=)



