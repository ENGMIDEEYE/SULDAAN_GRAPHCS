from django.contrib import admin
from blog.models import Category, Post, Visitors, Management

# Register your models here.

admin.site.register(Category),
admin.site.register(Post),
admin.site.register(Visitors),
admin.site.register(Management),

