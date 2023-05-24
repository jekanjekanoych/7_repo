from django.db import models
from students.models import Student
from teachers.models import Teacher


class Groups(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return "%s %s %s %i" % (self.name, self.teacher, self.students, self.id)