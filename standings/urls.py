from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'standings/$', views.index),
    #url(r'home', include('home.urls')),
    #path(r'admin/', admin.site.urls),
    #url(r'results', include('results.urls')),
]
