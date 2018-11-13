from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect, render

from APPS.account.models import Book, Classify
from APPS.shopcar.models import Shopcar
from APPS.shopcar.sum_count import book_count


def addcar(request):
    if request.is_ajax():
        user_id = request.user.id
        if user_id:
            book_id = request.POST.get('book_id')
            number = request.POST.get('number')
            query = Shopcar.objects.filter(user_id_id=user_id, book_id_id=book_id, is_delete=0)
            if query:
                q = query.first()
                q.count += int(number)
                q.save(update_fields=['count'])
            else:
                qw = Shopcar(book_id_id=book_id, count=number, user_id_id=user_id)
                qw.save()
            data = book_count(request)
            return JsonResponse(data=data)
        else:
            data = {"status": 405}
            return JsonResponse(data=data)


def show_car(request):
    user_id = request.user.id
    shopcars = Shopcar.objects.filter(user_id_id=user_id, is_delete=0).all()
    for shopcar in shopcars:
        book_id = shopcar.book_id_id
        books = Book.objects.filter(book_id=book_id).all()
        for book in books:
            shopcar.bookname = book.book_name
            shopcar.img_url = book.img_url
            classify_id = book.classify_id_id
            classify_name = Classify.objects.filter(classify_id=classify_id).first()
            book.classify_name = classify_name.classify_name
    return render(request, "shopcar_detail.html", {"shopcars": shopcars})


def delete_shopcar(request):
    if request.is_ajax():
        user_id = request.user.id
        if user_id:
            book_id = request.POST.get('book_id')
            shopcar = Shopcar.objects.get(user_id_id=user_id, book_id_id=book_id, is_delete=0)
            shopcar.is_delete = 1
            shopcar.save(update_fields=['is_delete'])
            return JsonResponse({'status': 200, 'msg': 'success'})
        else:
            return JsonResponse({'status': 404, 'msg': 'failed'})


def jian(request):
    try:
        book_id = request.POST.get('book_id')
        Shopcar.objects.filter(book_id_id=book_id, is_delete=0).update(count=F('count') - 1)
        return JsonResponse({'status': 200, 'msg': 'success'})
    except Exception as e:
        print(e)


def jia(request):
    try:
        book_id = request.POST.get('book_id')
        Shopcar.objects.filter(book_id_id=book_id, is_delete=0).update(count=F('count') + 1)
        return JsonResponse({'status': 200, 'msg': 'success'})
    except Exception as e:
        print(e)
