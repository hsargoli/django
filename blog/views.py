from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView, CreateView

from .models import blog_Post

class BlogView(ListView):
    model = blog_Post
    template_name = 'blog_template.html'

class BlogDetailView(DetailView):
    model = blog_Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): # new
    model = blog_Post
    template_name = 'post_new.html'
    fields = '__all__'

 


 
 
 
 
 
 
 
 
class hsargoli0(TemplateView):
    template_name = 'main.html'
    

class hsargoli2(TemplateView):
    template_name = 'main-slide-bar.html'
    
