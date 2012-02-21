from django.conf.urls.defaults import *

urlpatterns = patterns('data.views',
	url(r'^$', 'glowna'),
	url(r'^strony/(?P<strona_id>\d+)/$', 'strona'),
)
