from rest_framework import viewsets
from .models import Weight
from .serializers import WeightSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class WeightViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


