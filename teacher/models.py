from django.db import models

# Create your models here.
class Teachers(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    title = models.CharField(max_length=10)
    work_place = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    research_area = models.CharField(max_length=30)
    recruit_number = models.IntegerField()
    url = models.URLField()