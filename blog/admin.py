from django.contrib import admin
from .models import Post, Category

admin.site.register(Post) #register the newly created model
admin.site.register(Category)


