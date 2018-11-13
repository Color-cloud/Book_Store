from celery.task import task
from django.core.mail import send_mail  # 发送邮件模块

from Book_Store.settings import EMAIL_FROM  # setting.py添加的的配置信息


@task
def send_jihuo_email(uid):
    email = "2974941381@qq.com"
    email_title = "注册激活链接"
    email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/account/jihuo/?uid=%s" % uid
    send_mail(email_title, email_body, EMAIL_FROM, [email])
