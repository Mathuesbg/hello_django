from django.shortcuts import render
from .data import posts
from django.http import HttpResponse

def blog(request):
    context= {
        # "nome": "blog",
        "title" : "blog",
        "posts" : posts
    }
    return render(request=request, template_name="blog/index.html", context=context)

def post(request,id):
    return HttpResponse("oi")


def exemplo(request):
    context= {
        "nome": "exemplo",
        "title": "exemplo"
    }
    return render(request=request, template_name="blog/exemplo.html",context=context)