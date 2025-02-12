from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    return render(request, "blog/index.html")


def exemplo(request):
    return render(request, "blog/exemplo.html")