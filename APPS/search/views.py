from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from APPS.account.models import Book


def book_search(request):
    if request.method == 'POST':
        search_word = request.POST.get('book_search')
        search_books = Book.objects.filter(book_name__contains=search_word)
        return render(request, 'search_result.html', {'search_books': search_books})
