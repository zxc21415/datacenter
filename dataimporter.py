# 專門寫來轉資料的(從SQ3->MYSQL)

import os
import django
import sqlite3

from matplotlib.pyplot import title

# Django設定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import News

# STEP2 打開檔案

db = sqlite3.connect("nkustnews.db")
sql = "SELECT * from news;"
rows = db.execute(sql)
for row in rows:
    try:
        # STEP3 打開django的DB
        rec = News(title=row[1],
                content=row[2],
                pdate=row[3],
                url=row[4])
        # STEP4 write
        rec.save()
    except:
        pass
    print(row[1])
print("ALL done!")







#這是抓資料的
# authors = Author.objects.all()
# print(authors[:10])