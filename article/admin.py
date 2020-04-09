from django.contrib import admin
#导入models中的函数
from .models import ArticlePost

#注册ArticlePost到admin
admin.site.register(ArticlePost)

