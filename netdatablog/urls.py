from django.conf.urls import patterns, include, url
from django.contrib import admin
from index import index

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^blog/', include('blog.urls', namespace="blog")),
                       url(r'^admin/', include(admin.site.urls)),
)
