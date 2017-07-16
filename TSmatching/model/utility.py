from .models import Students, Teachers, Selection

# This class is used for checking the teacher users
# update the data of teacher in the database
class TeacherHandle:
    def __init__(self, name, pwd):
        self.__name = name
        self.__password = pwd

    # check the pwd of a teacher
    def can_login(self):
        try:
            result = Teachers.objects.filter(name=self.__name).values('password')
            if not result:
                return False
            else:
                return self.__password == result[0]['password']
        except Teachers.DoesNotExist:
            return False

    # Get information of the student
    def get_student_info(self, stu):
        stu_info_obj = Students.objects.get(user_name=stu.student.user_name)

        return {
            'Name': stu_info_obj.name,
            'School': stu_info_obj.university,
            'GPA': stu_info_obj.gpa,
            'Tel': stu_info_obj.phone_number,
            'Email': stu_info_obj.email,
            'Description': stu_info_obj.comment
        }

    # get the students that prefer this teacher
    def get_students(self):
        # Get the students that has not been accepted
        stu_list = Selection.objects.all().filter(student__accepted=False)

        # The result to store the students' info
        ret = []
        # Select out students that prefer this teacher now
        # we use deferred acceptance algorithm to determine which student should be expose
        # to this teacher
        for stu in stu_list:
            # check if the student has selected this teacher
            if stu.first.name == self.__name or\
                stu.second.name == self.__name or\
                stu.third.name == self.__name:
                # check stu's first preference
                if not stu.first_rejected:
                    stu_info = self.get_student_info(stu)
                    ret.append(stu_info)
                elif not stu.second_rejected:
                    stu_info = self.get_student_info(stu)
                    ret.append(stu_info)
                elif not stu.third_rejected:
                    stu_info = self.get_student_info(stu)
                    ret.append(stu_info)

        return ret

        # return [
        #     {
        #         'name': 'Test1',
        #         'school': 'Test University',
        #         'GPA': 3.67,
        #         'tel': '13233333333',
        #         'we_chat': 'test123',
        #         'photo': '/resource/photo/test.jpg',
        #         'description': '''
        #         Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
        #         richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
        #         Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
        #         sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
        #         Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
        #         proident.
        #         '''
        #     },
        #     {
        #         'name': 'Test2',
        #         'school': 'Test University',
        #         'GPA': 3.67,
        #         'tel': '13233333333',
        #         'we_chat': 'test123',
        #         'photo': '/resource/photo/test.jpg',
        #         'description': '''
        #         Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
        #         richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
        #         Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
        #         sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
        #         Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
        #         proident.
        #         '''
        #     },
        #     {
        #         'name': 'Test3',
        #         'school': 'Test University',
        #         'GPA': 3.67,
        #         'tel': '13233333333',
        #         'we_chat': 'test123',
        #         'photo': '/resource/photo/test.jpg',
        #         'description': '''
        #         Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
        #         richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
        #         Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
        #         sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
        #         Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
        #         proident.
        #         '''
        #     },
        #     {
        #         'name': 'Test4',
        #         'school': 'Test University',
        #         'GPA': 3.67,
        #         'tel': '13233333333',
        #         'we_chat': 'test123',
        #         'photo': '/resource/photo/test.jpg',
        #         'description': '''
        #         Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
        #         richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
        #         Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
        #         sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
        #         Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
        #         proident.
        #         '''
        #     }
        # ]
