from django.conf.urls import url

from APPS.book_detail import views

urlpatterns = [
    url('detail/',views.detail)
]
