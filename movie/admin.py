from django.contrib import admin
from .models import Movie,Review

# Register your models here.
admin.site.register(Movie)  #站点注册movie模型
admin.site.register(Review)
