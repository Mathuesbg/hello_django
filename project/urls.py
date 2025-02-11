from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from home.views import home
from blog.views import my_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  home),
    path('blog/',  my_view),
]


