from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/edit/',BlogUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',detail_of_page.as_view(), name='article_detail'), 
    path('<int:pk>/delete/',BlogDeleteView.as_view(), name='article_delete'),
    path('new/', BlogCreateView.as_view(), name='article_new'), 

    path('', models_view_page.as_view(), name='article_list'),
   ]
