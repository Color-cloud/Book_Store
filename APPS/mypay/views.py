import random
import time

from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import redirect
from Book_Store import settings


def pay(request):
    if request.method == "POST":
        smoney = request.POST.get('money')
        smoney = str(smoney)
        smoney = smoney[1:] + ".00"
        smoney = float(smoney)
        request.session["money"] = smoney
        return JsonResponse({"money": smoney})
    # 创建支付宝对象
    else:
        rand = str(time.time())
        c = rand.split('.')
        dingdan_num = c[0] + c[1] + str(random.randint(1, 99))
        money = float(request.session.get("money", 100))
        alipay = AliPay(appid=settings.APP_ID,
                        app_notify_url=None,
                        app_private_key_string=settings.APP_PRIVATE_STRING,
                        alipay_public_key_string=settings.APP_PUBLIC_STRING,
                        debug=True
                        )
        # 生成订单数据
        order_url = alipay.api_alipay_trade_page_pay(
            subject='测试支付TheOne',
            out_trade_no=dingdan_num,
            total_amount=money,
            # 支付成功后跳转到前端  get
            return_url='http://127.0.0.1:8000/',
            # 后台接受支付宝支付相关的信息的接口  post
            # notify_url=
        )
        pay_url = settings.ALI_PAY_DEV_URL + order_url
        return redirect(pay_url)


# 支付成功跳转的url
def notify_callback(request):
    pass
