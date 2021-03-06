from django.views.generic import ListView, TemplateView, DetailView, CreateView,UpdateView,DeleteView
from .models import blog
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied # new

class models_view_page(LoginRequiredMixin,ListView):
    model = blog
    template_name = 'article_list.html'
    login_url = 'login' # new
	
class detail_of_page(LoginRequiredMixin, DetailView):
    model = blog
    template_name = 'article_detail.html'
    login_url = 'login' 
	

class BlogUpdateView(LoginRequiredMixin, UpdateView): # new
    model = blog
    template_name = 'article_edit.html'
    fields = ['title', 'body']  # che fiekd hayi update she 
    login_url = 'login' # new
    def dispatch(self, request, *args, **kwargs):
     obj = self.get_object()
     if obj.author != self.request.user:
      raise PermissionDenied
     return super().dispatch(request, *args, **kwargs)
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = blog
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    #fields = '__all__' # for specify current to user we remove user in fields
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView): # new
    model = blog
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
     obj = self.get_object()
     if obj.author != self.request.user:
      raise PermissionDenied
     return super().dispatch(request, *args, **kwargs)