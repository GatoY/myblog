from django.shortcuts import get_object_or_404,render
from django.http import Http404,HttpResponse
from .models import Article

def index(request):
    article_list=Article.objects.order_by('-cre_date')
    context={'article_list':article_list}
    return render(request,'apps/index.html',context)
def detail(request,article_id):
    article=get_object_or_404(Article, pk=article_id)
    return render(request,'apps/detail.html',{'article':article})
