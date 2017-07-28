
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from .models import Students, Teachers, Selection

# This class is used for checking the teacher users
# update the data of teacher in the database
class TeacherHandle:
    def __init__(self, name, pwd=''):
        try:
            result = Teachers.objects.get(user_name=name)
            if not result:
                self.__can_login = False
            else:
                self.__name = result.user_name
                self.__password = result.password
                self.__id = result.id
                self.__can_login = self.__password == pwd
        except Teachers.DoesNotExist:
            self.__can_login = False

    def __str__(self):
        return self.__name

    # check the pwd of a teacher
    def can_login(self):
        return self.__can_login

    # Get information of the student
    @staticmethod
    def get_student_info(stu):
        stu_info_obj = Students.objects.get(user_name=stu)

        return {
            'name': stu_info_obj.name,
            'school': stu_info_obj.university,
            'GPA': stu_info_obj.gpa,
            'phone_number': stu_info_obj.phone_number,
            'we_chat': stu_info_obj.email,
            'description': stu_info_obj.comment,
            'photo': stu_info_obj.photo
        }

    # Get student object
    @staticmethod
    def get_student_obj(stu):
        # Get student object
        return Students.objects.get(name=stu)

    # get the students that prefer this teacher
    def get_students(self):
        # The result to store the students' info
        ret = []
        # Get the students that has not been accepted
        stu_list = Selection.objects.filter(student__accepted=0)

        # if no students choose this teacher, just return a empty dict
        if not stu_list.exists():
            return ret

        # Select out students that prefer this teacher now
        # we use deferred acceptance algorithm to determine which student should be expose
        # to this teacher
        # if this teacher has no more places, we'll reject all the students rest
        # tea_obj = Teachers.objects.get(id=self.__id)
        # if tea_obj.recruit_number <= 0:
        #     for stu in stu_list:
        #         self.reject(stu.student_id.name)
        #     return ret
        for stu in stu_list:
            # check if the student has selected this teacher
            # Check first choice
            if not stu.first_rejected:
                # According to DA algorithm,
                # student can apply for the teacher he prefer most,
                # while the teacher doesn't reject him
                if stu.first.user_name == self.__name:
                    ret.append(TeacherHandle.get_student_info(stu.student_id))
            elif not stu.second_rejected:
                if stu.second.user_name == self.__name:
                    ret.append(TeacherHandle.get_student_info(stu.student_id))
            elif not stu.third_rejected:
                if stu.third.user_name == self.__name:
                    ret.append(TeacherHandle.get_student_info(stu.student_id))

        return ret

    # Get the students this teacher has accepted
    def get_accepted_students(self):
        stu_list = Students.objects.filter(accepted=self.__id)
        ret = []
        for stu in stu_list:
            ret.append(TeacherHandle.get_student_info(stu.user_name))

        return ret

    # Accept the student:stu
    def accept(self, stu):
        # Get teacher object
        tea_obj = Teachers.objects.get(id=self.__id)
        # Judge whether this teacher can recruit more students
        if tea_obj.recruit_number <= 0:
            err = 'Your accepted students has up to limit, please reject one student and get to continue'
            return [False, err]

        # Get student object
        stu_obj = Students.objects.all().get(name=stu)
        # Set stu's adviser to this teacher
        stu_obj.accepted = self.__id

        # Decrease the recruit number of this teacher
        tea_obj.recruit_number = tea_obj.recruit_number - 1

        # Save all the changes
        stu_obj.save()
        tea_obj.save()

        return [True, '']

    # Reject the student stu
    def reject(self, stu, action):
        # Get student and teacher object
        tea_obj = Teachers.objects.get(id=self.__id)
        stu_obj = Students.objects.get(name=stu)
        # Update status of student
        stu_obj.accepted = 0
        # Update selection table
        stu_select = Selection.objects.get(student_id=stu_obj.user_name)
        # check whether
        if not stu_select.first_rejected and\
                stu_select.first.user_name == self.__name:
            stu_select.first_rejected = True
        elif not stu_select.second_rejected and\
                stu_select.second.user_name == self.__name:
            stu_select.second_rejected = True
        elif not stu_select.third_rejected and\
                stu_select.second.user_name == self.__name:
            stu_select.third_rejected = True
        if action == 'reject_ac' and tea_obj.recruit_number < 2:
            tea_obj.recruit_number = tea_obj.recruit_number + 1

        # Save all the changes
        stu_obj.save()
        tea_obj.save()
        stu_select.save()

class Captcha:
    def __init__(self, h, w):
        self.__height = h
        self.__width = w
        self.image = Image.new('RGB', (self.__width, self.__height), (255, 255, 255))
        self.chars = []


    def rndChar(self):
        return chr(random.randint(65, 90))

    def rndColor(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    def rndColor2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def captcha_generation(self):
        font = ImageFont.truetype('UbuntuMono-BI.ttf', 36)
        draw = ImageDraw.Draw(self.image)
        for x in range(self.__width):
            for y in range(self.__height):
                draw.point((x, y), fill=self.rndColor())
        for t in range(4):
            self.chars.append( self.rndChar())
            draw.text((50 * t + 10, 10),self.chars[t], font=font, fill=self.rndColor2())
        return self.chars
    def get_img(self):
        image = self.image.filter(ImageFilter.BLUR)
        return image

class NullDefault:
    def cleaned_data_not_null(self, label, current_form):
        if current_form.cleaned_data[label] is None:
            pass
