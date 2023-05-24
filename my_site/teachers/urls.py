from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/<int:id>", views.teacher, name="teacher"),
    path("new_teacher/", views.new_teacher, name="new_teacher"),
    path("delete_teacher/", views.delete_teacher, name="delete_teacher"),
]
