from django.contrib import admin


from .models import Article
from .models import Tag

class ArticleAdmin(admin.ModelAdmin) : 
	list_display = ('title', 'pub_date', 'update_time', )

class TagAdmin(admin.ModelAdmin) : 
    list_display = ('tag_name', )
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
# Register your models here.

