from django.shortcuts import render
from .data import posts

def blog(request):
    context= {
        "nome": "blog",
        "title" : "blog",
        "posts" : posts
    }
    return render(request=request, template_name="blog/index.html", context=context)


def exemplo(request):
    context= {
        "nome": "exemplo",
        "title": "exemplo"
    }
    return render(request=request, template_name="blog/exemplo.html",context=context)