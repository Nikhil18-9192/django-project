from django.urls import path

from restApi.Api import get_emp

app_name = 'emp'
urlpatterns = [
    # ex: /polls/
    path('get_emp/', get_emp.get_emp),
]
