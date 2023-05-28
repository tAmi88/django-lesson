from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def user_page(request):
    return render(request, 'user/users.html')


def filter_user(request):
    if request.method == 'GET':
        workers = Worker.objects.filter(name=request.GET.get('name'))
        
    return render(request, 'user/users.html', context={"workers": workers})