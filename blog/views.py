#coding : utf-8
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core import serializers
from collections import OrderedDict
#for model
from .models import Article
from .models import Tag

from bson import json_util
import json
import logging

page_size = 5

def index(request) : 
    return listBlogs(request)

def chuangHome(request):
	return render(request, 'chuangHome.html', {'select_module': 'profile', 'tag_cloud' : tagCloud()})

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
        articleDict['id'] = article[0].id
        logging.debug(article[0].id)
        articleDict['title'] = article[0].title
        articleDict['summary'] = article[0].summary
        articleDict['content'] = article[0].content
        articleDict['pub_date'] = article[0].pub_date.strftime("%Y-%m-%d-%H")
        articleDict['update_time'] = article[0].update_time.strftime("%Y-%m-%d-%H")
        return render(request, 'tecblog.html', {
            'article' : json.dumps(articleDict),
            'article_content' : articleDict['content'],
            'article_obj': article[0],
            'tag_cloud' : tagCloud(),
            })
    	pass

	return render(request, 'tecblog.html', {'tag_cloud' : tagCloud()} )

#Article List
def listBlogs(request):

    search_word = request.GET.get('search_word', "")
    page = int(request.GET.get('page', 1))

    article_set = []
    total_count = 0
    if(search_word is None or search_word == ""):
        article_set = listAllBlogs(page, page_size)
        total_count = getBlogCount()
    else:
        article_set = searchArticles(search_word, page, page_size)
        total_count = searchArticlesCount(search_word)

    pre_page = -1
    next_page = -1
    if page != 1:
        pre_page = page - 1
    if page * page_size <  total_count:
        next_page = page + 1    

    articleList = []
    jsonList = {}

    if len(article_set) != 0:
        for article in article_set:            
            # Basic properties for article
            tmpDict = {}
            tmpDict['title'] = article.title
            tmpDict['summary'] = article.summary
            tmpDict['key_words'] = article.key_words

            # Article Tag
            tmpTag = Tag.objects.filter(id=article.tag_id)
            if tmpTag:
                tmpDict['tag'] = tmpTag[0].tag_name
                tmpDict['tag_id'] = tmpTag[0].id
            else:
                # Never should be happened
                tmpDict['tag'] = 'Unknown'
                tmpDict['tag_id'] = -1

            articleList.append(tmpDict)
        #jsonList = serializers.serialize("json", article_set, fields=('title', 'summary'))
    jsonList = json.dumps(articleList)
    logging.debug(jsonList)
    return render(request, 'blogList.html', {
        'pre_page':pre_page, 
        'next_page': next_page,              
        'select_module': 'home', 
        'blogList' : json.loads(jsonList), 
        'tag_cloud' : tagCloud()
        })
    

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
    return render(request, 'archives.html', {
                                            'select_module': 'archive', 
                                            'dicts' : dicts, 
                                            'error' : False,
                                            'tag_cloud' : tagCloud()})

def listBlogByTag(request, tag_name):
    tag_id = request.GET.get('tag_id', -1)

    articleList = []
    if tag_id != -1:
        articleWithTag = Article.objects.filter(tag_id=tag_id)
        if articleWithTag :
            for article in articleWithTag:
                articleTitle = article.title
                articleList.append(articleTitle)
        return render(request, 'blogOfTag.html', {'articleList': articleList, 
                                                    'tag_cloud' : tagCloud(), 
                                                    'tag_name': tag_name})
    else :
        raise Http404 

def tagCloud() :
    try:
        tags = Tag.objects.all()
        tag_cloud = []
        for i in range(len(tags)):
            articleWithTag = Article.objects.filter(tag_id=tags[i].id)
            tmpDict = {}
            tmpDict['tag_name'] = tags[i].tag_name
            tmpDict['tag_id'] = tags[i].id
            if articleWithTag:
                tmpDict['count'] = len(articleWithTag)
            else :
                tmpDict['count'] = 0
            tag_cloud.append(tmpDict)
        logging.debug(tag_cloud);
        return json.dumps(tag_cloud)
    except Tag.DoesNotExist:
        raise Http404


# List All Articles 
def listAllBlogs(page, page_size): 
    start = (page - 1) * page_size
    end = start + page_size
    article_set = Article.objects.all()[start:end]
    return article_set

def getBlogCount(): 
    count = Article.objects.count()
    return count

def searchArticles(search_word, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    article_set = Article.objects.filter(title__icontains=search_word)[start:end]
    return article_set

def searchArticlesCount(search_word):
    count = Article.objects.filter(title__icontains=search_word).count()
    return count