from . import views
from django.urls import path

urlpatterns= [
    path("", views.PostList.as_view(), name="home"), #Here we use class based views , thats why we use 'as'
    path('<slug:slug>/' , views.PostDetail.as_view(), name='post_detail'),
]