from unicodedata import name
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

class CompanyType(models.Model):
    name = models.CharField(max_length=50,default="其他",verbose_name="類別")
    def __str__(self):
        return self.name

# 這個預設值是為了要更新公司資料用的，如果整個DB是全新的這個要刪掉還有下面default=get_defalut_ct
def get_defalut_ct():
    #name="其他業" 一定要CompanyType裡面有的不然會壞掉
    return CompanyType.objects.get(id=6).id

class Company(models.Model):
#公司資訊
    #後面才新增欄位，原本沒有的要幫他加上預設值，因為牽扯到外鍵，所以特別寫一個函式get_defalut_ct
    ct = models.ForeignKey(CompanyType,default=get_defalut_ct, on_delete=models.CASCADE,verbose_name="類別")
    #verbose_name列出來時，顯示的名稱
    code = models.CharField(max_length=10,verbose_name="編碼")
    name = models.CharField(max_length=20,verbose_name="名稱")


    def __str__(self):
        return self.name

class StockInfo(models.Model):
#股市資訊

    #公司=>外鍵
    #on_delete=models.CASCADE  外鍵來源被刪掉了，要怎麼做:一起刪掉
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name="公司名稱")
    dateinfo = models.DateField(verbose_name="日期")
    open_price = models.FloatField(verbose_name="開盤價")
    close_price = models.FloatField(verbose_name="收盤價")
    volume = models.PositiveIntegerField(verbose_name="數量")


    def __str__(self):
        return "({},{},{})".format(self.company,self.dateinfo,self.close_price)
