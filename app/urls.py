# This also imports the include function
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)