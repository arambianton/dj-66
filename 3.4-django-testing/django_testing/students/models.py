from django.db import models


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
        auto_now_add=True
    )


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )
