from django.contrib import admin
from mysite.models import News,Company,StockInfo   #匯入News類別
# Register your models here.

admin.site.register(News)
admin.site.register(Company)
admin.site.register(StockInfo)