from ..models import Article, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('cre_date')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('cre_date','year',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

