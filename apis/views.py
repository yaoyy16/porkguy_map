from rest_framework import viewsets

from .models import FundGet
from .serializers import FundGetSerializer


class FundGetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundGet.objects.all()
    serializer_class = FundGetSerializer
