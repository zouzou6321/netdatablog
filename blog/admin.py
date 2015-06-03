from django.contrib import admin
from blog.models import news

# Register your models here.


#class NewsAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'artic_text']

admin.site.register(news)
