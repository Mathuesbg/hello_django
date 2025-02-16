from django.urls import path
from blog.views import blog, exemplo,post

app_name = 'blog'

urlpatterns = [
    path('',  blog, name='blog'),
    path('<int:id>/',  post, name='post'),
    path('exemplo/',  exemplo, name='exemplo'),
]


