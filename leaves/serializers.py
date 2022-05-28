from rest_framework import serializers
from .models import Leave


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = [
            'id',
            'employee', 
            'start_date',
            'end_date',
            'date_created', 
            'type',
            'comments'
            ]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['employee'] = f'{instance.employee.first_name} {instance.employee.last_name}'
        return rep