from django.conf.urls import url

from APPS.shopcar import views

urlpatterns = [
    url("addcar/", views.addcar),
    url('show_car/', views.show_car, name='show_car'),
    url('delete_shopcar/', views.delete_shopcar, name='delete_shopcar'),
    url('jian/', views.jian, name='jian'),
    url('jia/', views.jia, name='jia'),
]
