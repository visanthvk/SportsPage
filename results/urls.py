from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'results/$', views.index),
    url(r'results/(?P<game>\D+)/$', views.index, name='display'),
    #url(r'standings/', include('sports.urls')),
    path(r'admin/', admin.site.urls),
    url(r'home', include('home.urls')),
]