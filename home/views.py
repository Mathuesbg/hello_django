from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        "nome": "home"
    }

    return render(
        request= request,
        template_name= 'home/index.html',
        context= context
        )
