from django.db import models
from employees.models import Employee
# Create your models here.

class Weight(models.Model):
    ROUND_CHOICES = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third')
    )
    date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    total_weight = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    weight_round = models.CharField(
        choices=ROUND_CHOICES,
        default='First',
        max_length=10
    )

    def __str__(self) -> str:
        return super().__str__(self.employee)



