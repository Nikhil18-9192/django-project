import json
from django.shortcuts import render
from .models import Student, Classroom
from django.core import serializers
from django.http import HttpResponse
# Create your views here.


def get_all_students(request):
    student_list = Student.objects.all().select_related('classroom_id')
    data = []
    for student in student_list:
        resp = {
            "name": student.name,
            "address": student.address,
            "percentage": student.percentage,
            "classroom": student.classroom_id.classroom_name
        }
        data.append(resp)
    return HttpResponse(json.dumps(data), content_type="application/json")
