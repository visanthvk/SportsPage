from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

app_name = 'sports'

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('home.urls')),
    url('home/', include('home.urls')),
    url('standings/', include('standings.urls')),
    url('results/', include('results.urls')),
    url('events/', include('events.urls')),
]
