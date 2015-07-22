from django.conf.urls import patterns, include, url
from django.contrib import admin
from map import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'porkguy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index),
	url(r'^generic', views.generic),
	url(r'^elements', views.elements),
]
