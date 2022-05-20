from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated

from accounts.models import User
from .models import Employee, Division
from .serializers import EmployeeSerializer, DivisionSerializer

# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DivisionViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class StatsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_count = User.objects.all().count()
        employees  = Employee.objects.all().count()
        divisions = Division.objects.all().count()
        data = {
            "users":user_count,
            "employees": employees,
            "divisions":divisions
        }   
        return Response(data)