from django.shortcuts import render

# Create your views here.
from APPS.account.models import *


def detail(request):
    if request.method == "GET":
        book_id = request.GET.get("book_id")
        book = Book.objects.filter(book_id=book_id)
        bookdetails = BookDetail.objects.filter(book_id=book_id)

        return render(request, 'detail.html', {'bookdetails': bookdetails,'book':book})
