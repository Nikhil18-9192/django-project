import json
from django.http import HttpResponse
from employee.models import Employee
from django.core import serializers

# Create your views here.


def addemployee(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        name = data['name']
        email = data['email']
        mobile = data['mobile']
        designation = data['designation']

        add_emp = Employee.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            designation=designation
        )

    return HttpResponse({'message: created'}, content_type="application/json")


def getemployee(request):
    data = serializers.serialize('json', Employee.objects.all())
    return HttpResponse(data, content_type="application/json")


def updateemployee(request, id):
    emp = Employee.objects.get(id=id)
    data = json.loads(request.body.decode("utf-8"))
    emp.name = data['name']
    emp.email = data['email']
    emp.mobile = data['mobile']
    emp.designation = data['designation']

    emp.save()

    return HttpResponse({'message: updated'}, content_type="application/json")


def deleteemployee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()

    return HttpResponse({'message: deleted'}, content_type="application/json")
