from django.contrib import admin
admin.autodiscover()

# import has to come after autodiscover, because we can't 
# unregister FlatPage until it's already been registered.
import app.admin

# This also imports the include function
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
