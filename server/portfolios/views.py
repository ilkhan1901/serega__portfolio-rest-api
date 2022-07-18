from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Portfolio.objects.all().order_by('-published')
    serializer_class = PortfolioSerializer

