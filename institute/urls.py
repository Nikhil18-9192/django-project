from django.urls import path

from . import views

app_name = 'institute'
urlpatterns = [
    path('', views.get_all_students, name='get_all_students'),
]
