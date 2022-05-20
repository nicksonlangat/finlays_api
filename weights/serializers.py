from rest_framework import serializers

from .models import Weight

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = [
            'id',
            'date', 
            'employee',
            'total_weight',
            'weight_round',
            ]
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['employee'] = f"{instance.employee.first_name} {instance.employee.last_name}" 
        return rep

