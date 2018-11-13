from django.conf.urls import url
from django.contrib import admin

from APPS.account import views

urlpatterns = [
    url("denglu",views.mylogin,name='denglu'),
    url("zhuce", views.zhuce),
    url('zhuxiao',views.my_logout),
    url('jihuo', views.jihuojiemian),
]
