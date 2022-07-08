from django.db import models

#寫完一定要  
# python manage.py makemigrations
# python manage.py migrate
# 我目前的資料庫是mynews

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pdate = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    class Meta:
        ordering = ('-pdate',)

    def __str__(self):
        return self.title

class Company(models.Model):
#公司資訊

    #verbose_name列出來時，顯示的名稱
    code = models.CharField(max_length=10,verbose_name="編碼")
    name = models.CharField(max_length=20,verbose_name="名稱")


    def __str__(self):
        return self.name

class StockInfo(models.Model):
#股市資訊

    #公司=>外鍵
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name="公司名稱")
    dateinfo = models.DateField(verbose_name="日期")
    open_price = models.FloatField(verbose_name="開盤價")
    close_price = models.FloatField(verbose_name="收盤價")
    volume = models.PositiveIntegerField(verbose_name="數量")


    def __str__(self):
        return "({},{},{})".format(self.company,self.dateinfo,self.close_price)
