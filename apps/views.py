from django.shortcuts import get_object_or_404,render
from django.http import Http404,HttpResponse
from .models import Article, Category, Twitterlist, Twitter, TwitterImg
import markdown
import pygments
import os
def index(request):
    article_list=Article.objects.order_by('-cre_date')
    context={'article_list':article_list}
    return render(request,'apps/index.html',context)
def detail(request,article_id):
    article=get_object_or_404(Article, pk=article_id)
    article.views+=1
    article.save()
    article.body=markdown.markdown(article.body,
				    extensions=[
				        'markdown.extensions.extra',
					'markdown.extensions.codehilite',
					'markdown.extensions.toc',
				    ])
    return render(request,'apps/detail.html',{'article':article})

def category(request):
    category_list=Category.objects.order_by('created_time')
    context={'category_list':category_list}
    return render(request,'apps/category.html', context)

def category_detail(request,category_id):
    cate=get_object_or_404(Category,pk=category_id)
    article_list=Article.objects.filter(category=cate)
    return render(request, 'apps/category_detail.html',context={'article_list':article_list})

def archive_detail(request,year):
    article_list=Article.objects.filter(cre_date__year=year)
    return render(request,'apps/index.html',context={'article_list':article_list})

def archive(request):
    archive_list = Article.objects.dates('cre_date','year',order='DESC')
    return render(request,'apps/archive.html',context={'archive_list': archive_list})
def twitterlist(request):
    twitter_list=Twitterlist.objects.order_by('-name')
    context={'twitter_list':twitter_list}
    return render(request,'apps/twitterlist.html',context)
def twitterdetail(request,twitter_id):
    twitter_name=get_object_or_404(Twitterlist, pk = twitter_id)
    twitter_list=Twitter.objects.filter(twittername=twitter_name).order_by('-pub_date')
    return render(request,'apps/twitterdetail.html',context={'twitter_name':twitter_name,'twitter_list':twitter_list})
def twittercontent(request,twitter_name_id,twitter_id):
    twitternumber=get_object_or_404(Twitter, pk=twitter_id)
    twitter_name=get_object_or_404(Twitterlist, pk = twitter_name_id)
    twitter_img=TwitterImg.objects.filter(twitter=twitternumber)
    return render(request,'apps/twittercontent.html',context={'twitter_name':twitter_name,'twitter_number':twitternumber,'twitterimg_list':twitter_img})

