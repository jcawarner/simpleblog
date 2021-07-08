from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255, default="Simple Blog")
	author = models.ForeignKey(User, on_delete=models.CASCADE)	#cascade- if user is deleted all posts are deleted with them
	body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=255, default='coding')

	def __str__(self):
		return self.title + ' | ' + str(self.author)  # see title and author of blog post in admin area

	def get_absolute_url(self):
		#return reverse('article-details', args=str(self.id)) -- redirects to the aritcle-details page
		return reverse('home') # redirect to the home page (dont need args)


class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):	
		return reverse('home') 

