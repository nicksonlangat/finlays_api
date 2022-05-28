from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from weights.models import Weight
from .models import Employee, Division
from .serializers import EmployeeSerializer, DivisionSerializer
from django.db.models import Sum
import datetime

class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DivisionViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
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


class PayrollView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']
        employees  = Employee.objects.all()
        now = datetime.datetime.now()
        total = 0
        details = {}
        data = []  
        for employee in employees:
            employee_weights =  Weight.objects.filter(employee=employee,
            date__gte=start_date,date__lte=end_date).all()
            weight = Weight.objects.filter(employee=employee,
            date__gte=start_date,date__lte=end_date).aggregate(total_weight=Sum('total_weight'))
            if weight:
                employee_data = {
                            "employee":f"{employee.first_name} {employee.last_name}",
                            "payroll_number":employee.payroll_number,
                            "total_weight":weight['total_weight'],
                            "earnings":weight['total_weight'] * 8,
                            "weights":[{"day": i.date, "weight": i.total_weight, "round": i.weight_round} for i in employee_weights]
                        }
            else:
                pass
            data.append(employee_data)
        for item in data:
            total += item['earnings']
        details['payroll_total'] = total
        details['payroll_from'] = start_date
        details['payroll_to'] = end_date
        data.append(details)

        return Response(data)