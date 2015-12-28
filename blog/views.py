#coding : utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core import serializers

#for model
from .models import Article

from bson import json_util
import json
import logging

def index(request) : 
    return listAllBlogs(request)

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
    #Get the article from database
    article = Article.objects.filter(title__iexact=title)
    logging.debug(article);
    
    #Generate Json Result
    if article:
        articleDict = {}
        articleDict['title'] = article[0].title
        articleDict['summary'] = article[0].summary
        articleDict['content'] = article[0].content
        articleDict['pub_date'] = article[0].pub_date.strftime("%Y-%m-%d-%H")
        articleDict['update_time'] = article[0].update_time.strftime("%Y-%m-%d-%H")
        return render(request, 'tecblog.html', {
            'article' : json.dumps(articleDict),
            'article_content' : articleDict['content']
            })
    	pass

	return render(request, 'tecblog.html')

#Article List
def listAllBlogs(request):
    article_set = Article.objects.all()

    articleList = []
    jsonList = {}

    if article_set:
        for article in article_set:
            tmpDict = {}
            tmpDict['title'] = article.title
            tmpDict['summary'] = article.summary
            articleList.append(tmpDict)
        #jsonList = serializers.serialize("json", article_set, fields=('title', 'summary'))
        jsonList = json.dumps(articleList)
        return render(request, 'blogList.html', {
            'blogList' : jsonList
            })

    return render(request, 'blogList.html')
