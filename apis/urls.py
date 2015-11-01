# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import FundGetViewSet

router = DefaultRouter()

router.register(r'lottery-fund', FundGetViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^docs/', include('rest_framework_swagger.urls')),
]
