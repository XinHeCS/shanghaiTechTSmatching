from django.db import models

# Create your models here.
class Students(models.Model):

    id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    university = models.CharField(max_length=25)
    gpa = models.FloatField()
    ranking = models.FloatField()
    comment = models.TextField()
    attachment = models.FileField(upload_to='attachment/%Y/%m/%d/')
    first_teacher = models.CharField(max_length=20)
    second_teacher = models.CharField(max_length=20)
    third_teacher = models.CharField(max_length=20)

class Selection(models.Model):
    student = models.ManyToManyField(Students,related_name="student")
    first_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher1")
    second_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher2")
    third_teacher = models.ManyToManyField('teacher.Teachers', related_name="teacher3")


