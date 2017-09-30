from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
app_name='apps'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^category/$',views.category,name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/$',views.category_detail,name='category_detail'),
    url(r'^archive/$',views.archive,name='archive'),
    url(r'^archive/(?P<year>[0-9]{4})/$',views.archive_detail,name='archive_detail'),
    url(r'^twitterlist/$',views.twitterlist,name='twitterlist'),
    url(r'^twitterlist/(?P<twitter_id>[0-9]+)/$',views.twitterdetail,name='twitterdetail'),
    url(r'^twittercontent/(?P<twitter_name_id>[0-9]+)/(?P<twitter_id>[0-9]+)/$',views.twittercontent,name='twittercontent'),
]
urlpatterns+=staticfiles_urlpatterns()

