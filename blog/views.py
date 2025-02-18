from django.shortcuts import render
from .data import posts
from django.http import Http404

def blog(request):
    context= {
        # "nome": "blog",
        "title" : "blog",
        "posts" : posts
    }
    return render(request=request, template_name="blog/index.html", context=context)

def post(request,id):
    found_post = None

    for post in posts:
        if post["id"] == id:
            found_post = post
            break
 
    if found_post is None:
        raise Http404('post nao existe')           
    
    context= {
        "title" : "post",
        "post" : found_post
    }        

    return render(request, template_name='blog/post.html', context=context)


def exemplo(request):
    context= {
        "nome": "exemplo",
        "title": "exemplo"
    }
    return render(request=request, template_name="blog/exemplo.html",context=context)