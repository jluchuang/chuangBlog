#coding : utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core import serializers

#for model
from .models import Article

import json
import logging

def index(request) : 
	return render(request, 'chuangHome.html')

def chuangHome(request):
	return render(request, 'chuangHome.html')

def jsonTest(request):
	List = ['find', 'study', 'try', 'work']
	Dict = {'site': 'keeptry.cn', 'author': 'chuang'}
	return render(request, 'jsonTest.html', { 
		'List' : json.dumps(List), 
		'Dict' : json.dumps(Dict)
	    })

def friends(request):
	return render(request, 'friends.html')

#Show content for article
def tecBlog(request, title):
	logging.debug(title)

	article_set = Article.objects.all()

	article = Article.objects.filter(title__iexact=title)
   
	if article:
		logging.debug(serializers.serialize("json", article))
    	pass

	return render(request, 'tecblog.html', {
		'article' : serializers.serialize("json", article),
		'blogList' : serializers.serialize("json", article_set)
		})

#Article List
def listAllBlogs(request):
    article_set = Article.objects.all()
    logging.debug(article_set)

    if article_set:
    	logging.debug(serializers.serialize("json", article_set))

	return render(request, 'blogList.html', {
		'blogList' : serializers.serialize("json", article_set)
		})
