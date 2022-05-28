from django.shortcuts import render, redirect
from .models import Category,Post
from django.views.generic.list import ListView
from .forms import ImageForm

class PostView(ListView):
   model = Post
   context_object_name = 'posts'
   template_name = 'myblog/post_view.html'


