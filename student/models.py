
from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# Create your models here.
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
    #attachment = models.FileField(upload_to='attachment/%Y/%m/%d/', default="")
    first_teacher = models.ManyToManyField('teacher.Teachers',null=True, related_name="teacher1")
    second_teacher = models.ManyToManyField('teacher.Teachers',null=True, related_name="teacher2")
    third_teacher = models.ManyToManyField('teacher.Teachers',null=True, related_name="teacher3")

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Students.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()