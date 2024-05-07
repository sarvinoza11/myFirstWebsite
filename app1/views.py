from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render

class Postview(ListView):
    model = Post
    template_name = "homepage.html"

class PostDetail(DetailView):
    model = Post
    template_name = 'detailpage.html'
    context_object_name = 'post'

class CreatePost(CreateView):
    model = Post
    template_name = 'Createpost.html'
    fields = ['title', 'text', 'author']

class EditPost(UpdateView):
    model = Post
    template_name = 'editpage.html'
    fields = ['title', 'text']

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepage.html'
    success_url = reverse_lazy('homepage')

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')