from rest_framework import viewsets
from .models import Weight
from .serializers import WeightSerializer

# Create your views here.

class WeightViewset(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


