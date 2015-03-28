from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.ArticListView.as_view(), name='list'),
                       url(r'^(?P<pk>\d+)/$', views.ArticDetailView.as_view(), name='detail'),
                       )
