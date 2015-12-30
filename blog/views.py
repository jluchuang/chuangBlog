#coding : utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core import serializers
from collections import OrderedDict
#for model
from .models import Article

from bson import json_util
import json
import logging

def index(request) : 
    return listBlogs(request)

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
            'article_content' : articleDict['content'],
            'article_obj': article[0],
            })
    	pass

	return render(request, 'tecblog.html')

#Article List
def listBlogs(request):

    search_word = request.GET.get('search_word', "")
    logging.debug(search_word)

    article_set = []
    if(search_word is None):
        article_set = listAllBlogs()
    else:
        article_set = searchArticles(search_word)

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

def archives(request) :
    try:
        post_date = Article.objects.dates('pub_date', 'month')
        post_date = post_date.reverse()
        post_date_article = []

        for i in range(len(post_date)):
            post_date_article.append([])
        for i in range(len(post_date)):
            cur_year = post_date[i].year
            cur_month = post_date[i].month
            temp_arc = Article.objects.filter(pub_date__year=cur_year).filter(pub_date__month = cur_month)
            post_date_article[i] = temp_arc

        dicts = OrderedDict()

        for i in range(len(post_date)):
            dicts.setdefault(post_date[i], post_date_article[i])
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'dicts' : dicts, 
                                            'error' : False})

# List All Articles 
def listAllBlogs(): 
    article_set = Article.objects.all()
    return article_set

def searchArticles(search_word):
    article_set = Article.objects.filter(title__icontains=search_word)
    return article_set