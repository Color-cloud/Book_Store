from django.shortcuts import render


def mybanner(request):
    return render(request, 'banners.html')
