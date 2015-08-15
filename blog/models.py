#coding : utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'title', max_length=256)
	summary = models.TextField(u'summary')
	content = models.TextField(u'content')

	pub_date = models.DateTimeField(u'pub_time', auto_now_add = True, editable = True)
	update_time = models.DateTimeField(u'update_time', auto_now = True, null = True)

	type_id =  models.IntegerField(u'type_id', default = 0)

	def __str__(self) : 
		return self.title 