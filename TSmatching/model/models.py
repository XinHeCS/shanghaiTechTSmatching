from django.db import models

# Create your models here.
# The teacher table
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

# The original student table
class Students(models.Model):
    user_name = models.CharField(max_length=20,default="",primary_key=True)
    resident_id = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=20, default="")
    sex = models.BooleanField(default=True)
    date_of_birth = models.DateField(default="1970-01-01")
    phone_number = models.CharField(max_length=25, default="")
    university = models.CharField(max_length=25, default="")
    major = models.CharField(max_length=25, default="")
    gpa = models.CharField(default="", max_length=10)
    email = models.EmailField(default="")
    ranking = models.CharField(default="", max_length=10)
    comment = models.TextField(default="")
    # True if this student has been accepted
    accepted = models.BooleanField(default=False)
    attachment = models.FileField(upload_to = './attachment', null=True)
    photo = models.ImageField(upload_to='./img', null=True)

    def __str__(self):
        return self.user_name

# Store the selection of students
class Selection(models.Model):
    # student name
    student = models.ForeignKey(Students, name='student', on_delete=models.CASCADE)

    # The preference of teachers that the student willing to select
    # the teacher this student would like to select first
    first_choice = models.ForeignKey(Teachers, name='first', on_delete=models.CASCADE)
    # whether the teacher of this choice has rejected this student
    # True means rejected
    # Note that False doesn't mean that the teacher has accepted this student.
    first_rejected = models.BooleanField(default=False)

    second_choice = models.ForeignKey(Teachers, name='second', on_delete=models.CASCADE)
    second_rejected = models.BooleanField(default=False)

    third_choice = models.ForeignKey(Teachers, name='third', on_delete=models.CASCADE)
    third_rejected = models.BooleanField(default=False)

    def __str__(self):
        self.student.__str__()

def file_name(name):
    pass
