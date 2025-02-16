from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    context= {
        "nome": "blog",
        "title" : "blog"
    }
    return render(request=request, template_name="blog/index.html", context=context)


def exemplo(request):
    context= {
        "nome": "exemplo",
        "title": "exemplo"
    }
    return render(request=request, template_name="blog/exemplo.html",context=context)