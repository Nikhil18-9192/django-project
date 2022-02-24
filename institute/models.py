from unicodedata import name
from django.db import models

# Create your models here.


class Classroom(models.Model):
    classroom_name = models.CharField(max_length=200)

    class Meta:
        db_table = "institute"


class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    percentage = models.IntegerField()
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
