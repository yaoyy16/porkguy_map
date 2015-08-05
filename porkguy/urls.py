from django.conf.urls import patterns, include, url
from django.contrib import admin
from map.views import showmap
from pages.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'porkguy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', home),
	url(r'^map/$', showmap),
]
