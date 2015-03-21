from django.contrib import admin
from blog.models import Artic

# Register your models here.


class ArticAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'artic_text']

admin.site.register(Artic, ArticAdmin)
