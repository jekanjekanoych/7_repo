from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from students.forms import StudentForm
from students.models import Student


def index(request):
    return HttpResponse("Student or Teacher does not exist")


def student(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect("index")
    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {"form": form}
        return render(request, "student.html", context)
    else:
        request.method == "POST"
    form = StudentForm(request.POST, instance=student)
    if not form.is_valid():
        return HttpResponse(reverse("new_student"))
    form.save()
    context = {"form": form}
    return render(request, "student.html", context)


def new_student(request):
    if request.method == "GET":
        form = StudentForm()
        context = {"form": form}
        return render(request, "new_student.html", context)
    else:
        request.method == "POST"
    form = StudentForm(request.POST)
    if not form.is_valid():
        return HttpResponse(reverse("new_student"))
    form.save()
    return HttpResponseRedirect(reverse("student", args=[form.instance.id]))


def delete_student(request):
    try:
        student = Student.objects.last()
        student.delete()
        students = Student.objects.all()
        return render(request, "delete_student.html", {"students": students})
    except AttributeError:
        return HttpResponseRedirect("/")
