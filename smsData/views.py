from django.shortcuts import render

from django.views.generic import ListView
from .models import *

# Create your views here.
class HomePageView(ListView):
    model = Sms
    template_name = 'homee.html'
    context_object_name = 'all_posts_list' # new
