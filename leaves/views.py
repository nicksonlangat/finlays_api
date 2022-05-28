from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Leave
from .serializers import LeaveSerializer

# Create your views here.

class LeaveViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
