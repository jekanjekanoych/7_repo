from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_to_group/", views.add_to_group, name="add_to_group"),
]
