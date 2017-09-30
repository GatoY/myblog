from django.contrib import admin
from .models import Article, Category, Tag, Twitterlist, Twitter, TwitterImg
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Twitterlist)
admin.site.register(Twitter)
admin.site.register(TwitterImg)
# Register your models here.
