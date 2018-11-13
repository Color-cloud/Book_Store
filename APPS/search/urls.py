from django.conf.urls import url
from django.contrib import admin

from APPS.search import views

urlpatterns = [
    url("search", views.book_search),
]
