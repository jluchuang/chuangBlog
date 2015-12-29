from django.contrib import admin


from .models import Article

class ArticleAdmin(admin.ModelAdmin) : 
	list_display = ('title', 'pub_date', 'update_time', )	

admin.site.register(Article, ArticleAdmin)
# Register your models here.

