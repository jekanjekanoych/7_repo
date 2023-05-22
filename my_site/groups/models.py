from django.db import models

class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return "%s %s %i %i" % (self.first_name, self.last_name, self.age, self.id)


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    # groups = models.ManyToManyField(Groups)

    def __str__(self):
        return "%s %s %i %i" % (self.first_name, self.last_name, self.age, self.id)

class Groups(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    students = models.ManyToManyField(Students)
    def __str__(self):
        return "%s %s %s %i" % (self.name, self.teacher, self.students, self.id)