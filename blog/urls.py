from django.urls import path 

from .views import *

urlpatterns = [ 
    path('',BlogView.as_view(), name = 'blog'),
    path('hs/',hsargoli0.as_view(), name ='hs0'),
    path('hs1/',hsargoli2.as_view(), name ='hs1'),
    path('post/new/',BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    ]