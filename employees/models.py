import math
import random
from django.db import models
from accounts.models import User
# Create your models here.

class Division(models.Model):
    name = models.CharField(
        max_length=255
    )
    division_manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    id_number = models.CharField(
        max_length=255
    )
    payroll_number = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.first_name
    
    def save(self, *args, **kwargs):
        val = math.floor(1000000 + random.random()*9000000)
        code = 'FN'+str(val*9)
        self.payroll_number=code 
        super(Employee, self).save(*args, **kwargs)
    