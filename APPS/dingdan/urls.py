from django.conf.urls import url

from APPS.dingdan import views

urlpatterns = [
    url('dingdan/',views.dingdan_detail,name='dingdan')
]
