from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'porkguy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ( r'^js/(?P<path>.*)$', 'map.views.static.serve',
    	{ 'document_root': 'D:/WORK/DMEATGUY/working/map/js' }),
	url(r'^$', 'map.views.home'),
)
