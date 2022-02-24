from django.urls import path

from . import views

app_name = 'institute'
urlpatterns = [
    path('', views.get_all_students, name='get_all_students'),
    path('max/', views.get_sutdent_of_high_percentage,
         name='get_sutdent_of_high_percentage'),
    path('min/', views.get_sutdent_of_low_percentage,
         name='get_sutdent_of_low_percentage'),
]
