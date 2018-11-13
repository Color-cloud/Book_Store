from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from APPS.account.models import *


def shouye(request):
    if request.method == "GET":
        classfy_id = request.GET.get('classfy_id')
        navigation = Classify.objects.all()
        if classfy_id:
            books = Book.objects.filter(classify_id=classfy_id)
        else:
            books = Book.objects.all()
        return render(request, "shouye.html", {"navs": navigation, "books": books})



