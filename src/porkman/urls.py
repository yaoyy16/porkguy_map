from django.conf.urls import include, url
from django.contrib import admin
from map.views import showmap
from pages.views import home, project_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'porkman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^map/$', showmap),
    url(r'^org/(?P<org_id>\d+)/$',
        project_detail,
        name='project_detail'),
    url(r'^api/', include('apis.urls')),
]
