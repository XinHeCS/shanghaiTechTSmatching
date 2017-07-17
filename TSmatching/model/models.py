from django.db import models
import requests
from lxml import html


# Create your models here.
# The teacher table
class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10,null=True)
    password = models.CharField(max_length=30)
    work_place = models.CharField(max_length=40, default=" ")
    name = models.CharField(max_length=100)
    email = models.EmailField(default=" ")
    phone_number = models.CharField(max_length=25,default=" ")
    research_area = models.CharField(max_length=100,default=" ")
    recruit_number = models.IntegerField(default=2)
    url = models.URLField()
    def __str__(self):
        return self.name

    def spider(self):
        url = "http://sist.shanghaitech.edu.cn/cn/Staff.asp?mid=22"
        self.teacher_info = []
        r = requests.get(url)
        r.encoding = 'utf-8'
        tree = html.fromstring(r.text)
        for i in range(2, 37):
            teacher_info_single = {}
            base_xpath = '//*[@id="lim"]/div/div[1]/div[2]/div[2]/div[' + str(i) + ']'
            teacher_info_single['name'] = tree.xpath(base_xpath + '/div[1]/a/text()')
            teacher_info_single['tel'] = tree.xpath(base_xpath + '/div[2]/span/text()[2]')
            if i == 2 or i == 33:
                teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[3]')
            # elif i == 34:
            #    teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[2]')
            else:
                teacher_info_single['email'] = tree.xpath(base_xpath + '/div[2]/span/text()[4]')

            teacher_info_single['address'] = tree.xpath(base_xpath + '/div[2]/span/text()[6]')
            if i >= 15 and i <= 16:
                teacher_info_single['area'] = ''.join(
                    tree.xpath(base_xpath + '/div[2]/span/ul/li[1]/span//text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[2]/span/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[3]/span/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/ul/li[4]/span/text()'))
            elif i == 14:
                teacher_info_single['area'] = ''.join(
                    tree.xpath(base_xpath + '/div[2]/span/div/ul/li[1]/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/div/ul/li[2]/text()')
                    + tree.xpath(base_xpath + '/div[2]/span/div/ul/li[3]/text()'))
            else:
                teacher_info_single['area'] = ''.join(
                    tree.xpath(base_xpath + '/div[2]/span/ul/li[1]/text()[1]') + tree.xpath(base_xpath
                                                                                            + '/div[2]/span/ul/li[2]/text()[1]') + tree.xpath(
                        base_xpath + '/div[2]/span/ul/li[3]/text()[1]') + tree.xpath(
                        base_xpath + '/div[2]/span/ul/li[4]/text()')).replace("\t", "").replace("\r", "")
            self.teacher_info.append(teacher_info_single)

    def save_spider_data(self):
        i = 2
        for each_teacher in self.teacher_info:
            # create entry in teacher
            print(each_teacher)
            print(i)
            teacher_info = Teachers(id=i)
            teacher_info.name=each_teacher['name'][0].strip(' ')
            teacher_info.phone_number=each_teacher['tel'][0].strip(' ')
            teacher_info.email=each_teacher['email'][0].strip(' ')
            teacher_info.work_place= " " if i==18 else each_teacher['address'][0].strip(' ')
            teacher_info.research_area=each_teacher['area'].strip(' ')[0:199]
            teacher_info.save()
            i = i + 1

# The original student table
class Students(models.Model):
    user_name = models.CharField(max_length=20, default="", primary_key=True)
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
    accepted = models.IntegerField(default=0)
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
    first_choice = models.ForeignKey(Teachers, name='first', on_delete=models.CASCADE, null=True)
    # whether the teacher of this choice has rejected this student
    # True means rejected
    # Note that False doesn't mean that the teacher has accepted this student.
    first_rejected = models.BooleanField(default=False)

    second_choice = models.ForeignKey(Teachers, name='second', on_delete=models.CASCADE, null=True)
    second_rejected = models.BooleanField(default=False)

    third_choice = models.ForeignKey(Teachers, name='third', on_delete=models.CASCADE, null=True)
    third_rejected = models.BooleanField(default=False)

    def __str__(self):
        self.student.__str__()


def file_name(name):
    pass
