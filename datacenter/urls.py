"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    #去mongodb拿資料
    path('api/mongo/<str:keyword>/', views.api_mongodb),
    #提供JSON
    path('mongodb-test/', views.mongodb_test),
    #提供JSON
    path('jquery-test/', views.jquery_test),
    #提供JSON
    path('api/stock/<str:code>/', views.api_stock),
    #字詞統計
    path('chart/', views.chart),
    #告訴她沒有跟數字的也可以接收
    path('stockinfo/', views.stockinfo),
    #個股歷代交易資訊頁面
    path('stockinfo/<int:id>/', views.stockinfo),
    #股票的公司
    path('company/<int:id>/', views.company),
    #股票類別呈現頁面
    path('stock/', views.stock),
    #分頁
    path('page/<int:pg>/', views.page),
    #新聞頁面
    path('show/<int:id>/', views.show),
    path('lotto/', views.lotto),

    path('admin/', admin.site.urls),

    # path('/?p=<int:p>/', views.index),

    #如果沒有說要去哪=去首頁
    path('', views.index),
]
