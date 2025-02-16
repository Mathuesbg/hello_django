from django.urls import path
from blog.views import blog, exemplo

app_name = 'blog'

urlpatterns = [
    path('',  blog, name='blog'),
    path('exemplo/',  exemplo, name='exemplo'),
]


