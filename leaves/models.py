from django.db import models

from employees.models import Employee

# Create your models here.
class Leave(models.Model):
    TYPE_CHOICES = (
        ('Sick Leave', 'Sick Leave'),
        ('Annual Leave', 'Annual Leave'),
        ('Maternity Leave', 'Maternity Leave')
    )
    date_created = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(
        choices=TYPE_CHOICES,
        default='Sick Leave',
        max_length=20
    )
    comments = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return super().__str__(self.employee)
