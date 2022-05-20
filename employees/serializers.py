from rest_framework import serializers

from employees.models import Division, Employee

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = [
            'id',
            'name', 
            'division_manager',
            ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name', 
            'last_name',
            'phone_number',
            'id_number', 
            'payroll_number',
            'division'
            ]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['division'] = instance.division.name
        return rep