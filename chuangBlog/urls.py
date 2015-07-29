from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chuang.views.index', name='home'),
    url(r'^chuangHome/$', 'chuang.views.chuangHome', name='chuangHome'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jsonTest/$', 'chuang.views.jsonTest', name = 'jsonTest'),

    url(r'^qrcode/$', 'tools.views.generate_qrcode', name = 'qrcode'), 

    url(r'^admin/', include(admin.site.urls)),

    url(r'^css/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root':'/home/chuang/chuangBlog/chuang/templates/css'}),

    url(r'^js/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root':'/home/chuang/chuangBlog/chuang/templates/js'}),
)
