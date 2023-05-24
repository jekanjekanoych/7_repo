from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from groups.forms import GroupsForm
from groups.models import Groups


def index(request):
    return HttpResponse("Student or Teacher does not exist")


def add_to_group(request):
    if request.method == "GET":
        form = GroupsForm()
        context = {"form": form}
        return render(request, "add_to_group.html", context)
    else:
        request.method == "POST"
    form = GroupsForm(request.POST)
    if not form.is_valid():
        return HttpResponse(reverse("index"))
    form.save()
    return HttpResponseRedirect(reverse("add_to_group"))
