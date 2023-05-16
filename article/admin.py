from django.contrib import admin

# Register your models here.
# 别忘了导入ArticlerPost
from article.models import Article, Category

# 注册ArticlePost到admin中
admin.site.register(Article)
admin.site.register(Category)