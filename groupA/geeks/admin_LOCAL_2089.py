from django.contrib import admin
from .models import category, Post, forbidden
# Register your models here.
admin.site.register(Post)
admin.site.register(category)

