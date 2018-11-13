from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from APPS.account.task import send_jihuo_email


def mylogin(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    elif request.method == 'POST':
        username = request.POST.get('srusername')
        password = request.POST.get('srpassword')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login_page.html', {'msg': '用户名或密码输入错误'})


def zhuce(request):
    if request.method == 'GET':
        return render(request, 'zhuce_page.html')
    elif request.method == 'POST':
        username = request.POST.get('zcusername')
        password = request.POST.get('zcpassword')
        qr = request.POST.get('qrpassword')
        if qr == password:
            a = User.objects.create_user(username=username, password=password, is_active=0)
            uid = a.id
            send_jihuo_email(uid)
        else:
            return render(request, 'zhuce_page.html', {'msg': '两次输入密码不一致'})
        return redirect('/')


def my_logout(request):
    auth.logout(request)
    return redirect('/')


def jihuojiemian(request):
    uid = request.GET.get("uid")
    u_query = User.objects.filter(id=uid).first()
    u_query.is_active = 1
    u_query.save(update_fields=['is_active'])
    return redirect("/account/denglu", {"message": "激活成功!"})
