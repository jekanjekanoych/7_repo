from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from teachers.forms import TeacherForm
from teachers.models import Teacher


def index(request):
    return HttpResponse("Teacher or Student does not exist")


def teacher(request, id: int):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponseRedirect("index")
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        context = {"form": form}
        return render(request, "teacher.html", context)
    else:
        request.method == "POST"
    form = TeacherForm(request.POST, instance=teacher)
    if not form.is_valid():
        return HttpResponse(reverse("new_teacher"))
    form.save()
    context = {"form": form}
    return render(request, "teacher.html", context)


def new_teacher(request):
    if request.method == "GET":
        form = TeacherForm()
        context = {"form": form}
        return render(request, "new_teacher.html", context)
    else:
        request.method == "POST"
    form = TeacherForm(request.POST)
    if not form.is_valid():
        return HttpResponse(reverse("new_teacher"))
    form.save()
    return HttpResponseRedirect(reverse("teacher", args=[form.instance.id]))


def delete_teacher(request):
    try:
        teacher = Teacher.objects.last()
        teacher.delete()
        teachers = Teacher.objects.all()
        # form = StudentForm(instance=students)
        return render(request, "delete_teacher.html", {"teachers": teachers})
    #     return HttpResponseRedirect("/")
    except AttributeError:
        return HttpResponseRedirect("/")


#
