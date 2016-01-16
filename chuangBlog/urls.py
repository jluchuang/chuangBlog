from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    # Ckeditor upload file path
    url(r'^media/(?P<path>.*)$','django.views.static.serve', 
        {'document_root':'/home/chuang/chuangBlog/media'}),

    # Ckeditor upload file path
    url(r'^static/(?P<path>.*)$','django.views.static.serve', 
        {'document_root':'/home/chuang/chuangBlog/static'}),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
    
    # For ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    # Home 
    url(r'^$', 'blog.views.index', name='home'),

    # Tec Blog
    url(r'^blogList/(.+)/$', 'blog.views.tecBlog', name='tecblog'),

    # Blog List
    url(r'^blogList/$', 'blog.views.listBlogs', name='blogList'),

    # About me
    url(r'^aboutMe/$', 'blog.views.chuangHome', name='aboutMe'),

    # Friends
    url(r'^friends/$', 'blog.views.friends', name='friends'),

    # Just some study
    url(r'^jsonTest/$', 'blog.views.jsonTest', name = 'jsonTest'),

    url(r'^archives/$', 'blog.views.archives', name = 'archives'),

    url(r'^tagList/(.+)/$', 'blog.views.listBlogByTag', name = 'tagList'),
)
