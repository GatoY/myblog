from django.conf.urls import url
from . import views
app_name='apps'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^category/$',views.category,name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/$',views.category_detail,name='category_detail'),
]

