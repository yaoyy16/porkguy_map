# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import FundGetViewSet, LotteryStoreViewSet, SurplusViewSet

router = DefaultRouter()

router.register(r'fund-project', FundGetViewSet)
router.register(r'lottery-store', LotteryStoreViewSet)
router.register(r'lottery-surplus', SurplusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
