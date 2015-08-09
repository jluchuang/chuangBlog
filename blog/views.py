#coding : utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#for model
from .models import Article

import json

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

def tecBlog(request):
	return render(request, 'tecblog.html')

def listAllBlogs(request):
    articles = Article.objects.all()
    blogList = []
    for article in articles:
    	blogList.append(article.title)

	return render(request, 'blogList.html', {
		'blogList' : json.dumps(blogList)
		})