from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    #For the common sources 
    url(r'^css/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root':'/home/chuang/chuangBlog/common/css'}),

    url(r'^js/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root':'/home/chuang/chuangBlog/common/js'}),

    url(r'^inc/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root':'/home/chuang/chuangBlog/common/inc'}),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', 
        {'document_root':'/home/chuang/chuangBlog/common/media'}),
    
    #Home 
    url(r'^$', 'blog.views.index', name='home'),

    #About me
    url(r'^aboutMe/$', 'blog.views.chuangHome', name='aboutMe'),

    #About me
    url(r'^friends/$', 'blog.views.friends', name='friends'),

    #Admin
    url(r'^admin/', include(admin.site.urls)),

    #Tools
    url(r'^qrcode/$', 'tools.views.generate_qrcode', name = 'qrcode'),

    #Just some study
    url(r'^jsonTest/$', 'blog.views.jsonTest', name = 'jsonTest'),
)
