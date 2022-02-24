import json
from django.shortcuts import render
from .models import Student, Classroom
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Max, Min
# Create your views here.


def get_all_students(request):
    student_list = Student.objects.all().select_related('classroom_id')
    data = []
    for student in student_list:

        resp = {
            "name": student.name,
            "address": student.address,
            "percentage": student.percentage,
            "classroom": student.classroom_id.classroom_name,
            "classroom_id": student.classroom_id.id
        }
        data.append(resp)
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_sutdent_of_high_percentage(request):
    max_percent = Student.objects.all().aggregate(Max('percentage'))
    students = Student.objects.filter(
        percentage=max_percent['percentage__max']).select_related('classroom_id')

    for student in students:
        resp = {
            "name": student.name,
            "address": student.address,
            "percentage": student.percentage,
            "classroom": student.classroom_id.classroom_name,
            "classroom_id": student.classroom_id.id
        }

    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_sutdent_of_low_percentage(request):
    max_percent = Student.objects.all().aggregate(Min('percentage'))
    students = Student.objects.filter(
        percentage=max_percent['percentage__min']).select_related('classroom_id')

    for student in students:
        resp = {
            "name": student.name,
            "address": student.address,
            "percentage": student.percentage,
            "classroom": student.classroom_id.classroom_name,
            "classroom_id": student.classroom_id.id
        }

    return HttpResponse(json.dumps(resp), content_type="application/json")
