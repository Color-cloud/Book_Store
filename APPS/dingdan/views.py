import random
import time

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from APPS.account.models import Book
from APPS.dingdan.models import DingDan
from APPS.shopcar.models import Shopcar


def dingdan_detail(request):
    if request.is_ajax:
        if request.method == "POST":
            shop_list = []
            book_ids = request.POST.get('1book_ids')
            zong_e = request.POST.get('zong_e')
            shop_lists = book_ids.strip(',').split(',')  # 将一个字符串转化为一个列表
            for shop in shop_lists:
                try:
                    qset_json = serializers.serialize("json", Shopcar.objects.filter(book_id_id=int(shop[1:])).all())
                    shop_list.append(qset_json)
                    qs = Shopcar.objects.filter(book_id_id=int(shop[1:])).all()
                    for q in qs:
                        q.is_delete = 1
                        q.save(update_fields=["is_delete"])
                except Exception as e:
                    print(e)

            return JsonResponse({'status': 200, 'shop_list': shop_list, "money_total": zong_e})
        # 该返回的shop_list 格式为[{"q":"w"}],[{"q":"w"}],[{"q":"w"}]....
        elif request.method == "GET":
            # ajax全局跳转方式是GET请求
            uid = request.user.id
            rdata = request.GET.get("rdata")
            zong_e = request.GET.get("zong_e")
            rdata = eval(rdata)
            querys = []
            rand = str(time.time())
            c = rand.split('.')
            dingdan_num = c[0] + c[1] + str(random.randint(1, 99))

            for data in rdata:
                try:
                    for query in data:
                        book_id = query['fields']['book_id']
                        books = Book.objects.filter(book_id=book_id).all()
                        for book in books:
                            book.danjia = Shopcar.objects.filter(book_id_id=book_id).first().price
                            book.shuliang = Shopcar.objects.filter(book_id_id=book_id).first().count
                        querys.append(books)
                        DingDan.objects.create(book_id_id=book_id, user_id_id=uid, dingdan_number=dingdan_num)
                except Exception as e:
                    book_id = data['fields']['book_id']
                    books = Book.objects.filter(book_id=book_id).all()
                    for book in books:
                        book.danjia = Shopcar.objects.filter(book_id_id=book_id).first().price
                        book.shuliang = Shopcar.objects.filter(book_id_id=book_id).first().count
                    querys.append(books)
                    DingDan.objects.create(book_id_id=book_id, user_id_id=uid, dingdan_number=dingdan_num)
            return render(request, "dingdan.html", {"querys": querys, "dingdan_num": dingdan_num, "zong_e": zong_e})
