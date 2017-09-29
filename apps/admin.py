from django.contrib import admin
from .models import Article, Category, Tag, Twitterlist
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Twitterlist)
# Register your models here.
