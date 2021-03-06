from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']
	#ordering = ['-id'] # the order that posts appear on the page


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'


class AddPostView(CreateView):
	model = Post
	form_class = PostForm  #takes care of fields for us
	template_name = 'add_post.html'
	#fields = '__all__'  -- returns all fields of my model
	#fields = ('title', 'body')  # returns variation of fields you pick


class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'  
	


class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' ') ,'category_posts': category_posts})
