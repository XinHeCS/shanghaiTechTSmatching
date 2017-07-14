from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Students(User):
    resident_id = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=20, default="")
    date_of_birth = models.DateField(default="")
    phone_number = models.CharField(max_length=25, default="")
    university = models.CharField(max_length=25, default="")
    major = models.CharField(max_length=25, default="")
    gpa = models.FloatField(default="")
    ranking = models.FloatField(default="")
    comment = models.TextField()
    attachment = models.FileField(upload_to='attachment/%Y/%m/%d/')
    first_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher1")
    second_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher2")
    third_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher3")
