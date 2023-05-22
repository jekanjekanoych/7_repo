from django import forms
from .models import Groups


class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ["name", "teacher", "students"]
