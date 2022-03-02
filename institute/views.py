import json
from django.shortcuts import render
from .models import Student, Classroom
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Max, Min
# Create your views here.


def create_student(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        selected_classroom = Classroom.objects.get(id=data['classroom_id'])
        name = data['name']
        address = data['address']
        percentage = data['percentage']
        classroom_id = selected_classroom

        add_student = Student.objects.create(
            name=name,
            address=address,
            percentage=percentage,
            classroom_id=classroom_id
        )

    return HttpResponse({'message: created'}, content_type="application/json")


def update_student(request, id):
    student = Student.objects.get(id=id)
    data = json.loads(request.body.decode("utf-8"))
    selected_classroom = Classroom.objects.get(id=data['classroom_id'])
    student.name = data['name']
    student.address = data['address']
    student.percentage = data['percentage']
    student.classroom_id = selected_classroom

    student.save()

    return HttpResponse({'message: updated'}, content_type="application/json")


def delete_student(request, id):
    if request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()

    return HttpResponse({'message: deleted'}, content_type="application/json")


def get_all_students(request):
    student_list = Student.objects.all().select_related('classroom_id')
    data = []
    for student in student_list:

        resp = {
            "student_id": student.id,
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


def create_classroom(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        classroom_name = data['classroom_name']
        add_classroom = Classroom.objects.create(
            classroom_name=classroom_name
        )

    return HttpResponse({'message: created'}, content_type="application/json")


def get_all_classroom(request):
    if request.method == 'GET':
        data = Classroom.objects.all()
        resp = [
        ]
        for item in data:
            obj = {
                "classrrom_id": item.id,
                "classroom_name": item.classroom_name
            }

            resp.append(obj)

    return HttpResponse(json.dumps(resp), content_type="application/json")


def update_classroom(request, id):
    if request.method == 'POST':
        data = Classroom.objects.get(id=id)
        res = json.loads(request.body.decode("utf-8"))

        data.classroom_name = res["classroom_name"]

        data.save()

    return HttpResponse({'message: updated'}, content_type="application/json")


def student_by_address(request):
    if request.method == 'GET':
        data = serializers.serialize(
            'json', Student.objects.filter(address='pune'))
        print(data)

    return HttpResponse(data, content_type="application/json")


def get_all_students_classroom_count(request):
    if request.method == 'GET':
        data = Student.objects.all().values(
            'classroom_id')
        count = 0
        id = 0
        for item in data:
            if item['classroom_id'] != id:
                id = item['classroom_id']
                count = count + 1

    return HttpResponse(count, content_type="application/json")
