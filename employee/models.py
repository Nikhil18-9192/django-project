from django.db import models
import datetime
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"
