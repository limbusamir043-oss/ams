from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path("teacher/assignments/", views.assignment_list, name="teacher_assignments_list"),
    path("teacher/assignments/create/", views.create_assignment, name="teacher_assignments"),
    path("teacher/assignments/<int:pk>/edit/", views.edit_assignment, name="edit_assignment"),
    path("teacher/assignments/<int:pk>/delete/", views.delete_assignment, name="delete_assignment"),
    path("student/assignments/", views.student_assignments, name="student_assignments"),
]

   

