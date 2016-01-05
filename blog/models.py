#coding : utf-8
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Tag(models.Model):
    #id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(u'tag_name', max_length=256)

    def __str__(self):
        return self.tag_name
        pass
        

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'title', max_length=256)
    summary = models.TextField(u'summary')
    content = RichTextField(u'content', config_name = 'default')

    pub_date = models.DateField(u'pub_time', auto_now_add = True, editable = True)
    update_time = models.DateField(u'update_time', auto_now = True, null = True)

    tag =  models.ForeignKey(Tag)
    key_words = models.CharField(u'key_words', max_length=256)

    def __str__(self) : 
        return self.title 
