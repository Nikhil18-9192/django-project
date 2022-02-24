from django.urls import path

from . import views

app_name = 'employee'
urlpatterns = [
    # ex: /polls/
    path('', views.getemployee, name='getemployee'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('updateemployee/<int:id>', views.updateemployee, name='updateemployee'),
    path('deleteemployee/<int:id>', views.deleteemployee, name='deleteemployee'),
]
