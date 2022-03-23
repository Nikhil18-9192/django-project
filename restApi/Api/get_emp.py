from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponse
from django.core import serializers
from restApi.models import Emp


@api_view(['GET'])
def get_emp(request):
    if request.method == 'GET':
        response = serializers.serialize('json', Emp.objects.all())

        return HttpResponse(response, content_type="application/json")
