from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('blog do app')


def exemplo(request):
    return HttpResponse('exemplo do app')