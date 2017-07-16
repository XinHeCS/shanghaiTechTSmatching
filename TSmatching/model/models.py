from django.db import models

# Create your models here.
class Teachers(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    title = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    work_place = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    research_area = models.CharField(max_length=30)
    recruit_number = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.name

class Students(models.Model):
    user_name = models.CharField(max_length=20,default="",primary_key=True)
    resident_id = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=20, default="")
    date_of_birth = models.DateField(default="1970-01-01")
    phone_number = models.CharField(max_length=25, default="")
    university = models.CharField(max_length=25, default="")
    major = models.CharField(max_length=25, default="")
    gpa = models.CharField(default="", max_length=10)
    email = models.EmailField(default="")
    ranking = models.CharField(default="", max_length=10)
    comment = models.TextField(default="")

    def __str__(self):
        return self.user_name
