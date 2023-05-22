from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("student/<int:id>", views.student, name="student"),
    path("new_student/", views.new_student, name="new_student"),
    path("delete_student/", views.delete_student, name="delete_student"),
]
