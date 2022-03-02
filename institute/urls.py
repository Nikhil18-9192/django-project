from django.urls import path

from . import views

app_name = 'institute'
urlpatterns = [
    path('', views.get_all_students, name='get_all_students'),
    path('max/', views.get_sutdent_of_high_percentage,
         name='get_sutdent_of_high_percentage'),
    path('min/', views.get_sutdent_of_low_percentage,
         name='get_sutdent_of_low_percentage'),
    path('student_create/', views.create_student,
         name='create_student'),
    path('student_update/<int:id>', views.update_student, name='update_student'),
    path('student_delete/<int:id>', views.delete_student, name='delete_student'),
    path('classroom_create/', views.create_classroom,
         name='create_classroom'),
    path('get_all_classroom/', views.get_all_classroom,
         name='get_all_classroom'),
    path('classroom_update/<int:id>',
         views.update_classroom, name='update_classroom'),
    path('get_student_by_address',
         views.student_by_address, name='student_by_address'),
    path('get_student_classroom_count',
         views.get_all_students_classroom_count, name='get_all_students_classroom_count'),
]
