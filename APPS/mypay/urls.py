from django.conf.urls import url

from APPS.mypay import views

urlpatterns = [
    url('alipay/', views.pay, name='pay'),
]
