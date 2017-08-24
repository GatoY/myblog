from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

from django.utils import timezone
class Article(models.Model):
	title=models.CharField('title',max_length=100)
	body=models.TextField('body')
	cre_date=models.DateTimeField('date created',auto_now_add=True)
	modi_date=models.DateTimeField('date modified',auto_now=True)
	#abstract=models.CharField('abstract',max_length=54,blank=True,null=True,help_text="optional, default to get 54 characters in body")
	views=models.PositiveIntegerField('views',default=0)
	likes=models.PositiveIntegerField('likes',default=0)
	#category=models.ForeignKey('Category',verbose_name='category',null=True,on_delete=models.SET_NULL)
	#tags=models.ManyToManyField('Tag',verbose_name='tags group',blank=True)
	def __str__(self):
		return self.title
