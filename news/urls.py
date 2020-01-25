from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='news_url'),
    path('tag/<str:pk>/', TagDetail.as_view(), name='tag_detail_url'),
    path('post/<str:pk>/', PostBody.as_view(), name='post_detail_url'),
    path('lazy_load_posts/', lazy_load_posts, name='lazy_load_posts'),
]