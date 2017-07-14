from .models import Students, Teachers

# This class is used for checking the teacher users
# update the data of teacher in the database
class TeacherHandle:
    def __init__(self, name, pwd):
        self.__name = name
        self.__password = pwd

    # check the pwd of a teacher
    def can_login(self):
        try:
            result = Teachers.objects.filter(name=self.__name).values('phone_number')
            if not result:
                return False
            else:
                return self.__password == result[0]['phone_number']
        except Teachers.DoesNotExist:
            return False

    # get the students that prefer current teacher
    def get_students(self):
        return [
            {
                'name': 'Test1',
                'school': 'Test University',
                'GPA': 3.67,
                'tel': '13233333333',
                'we_chat': 'test123',
                'photo': '/resource/photo/test.jpg',
                'description': '''
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
                Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
                sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
                proident.
                '''
            },
            {
                'name': 'Test2',
                'school': 'Test University',
                'GPA': 3.67,
                'tel': '13233333333',
                'we_chat': 'test123',
                'photo': '/resource/photo/test.jpg',
                'description': '''
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
                Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
                sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
                proident.
                '''
            },
            {
                'name': 'Test3',
                'school': 'Test University',
                'GPA': 3.67,
                'tel': '13233333333',
                'we_chat': 'test123',
                'photo': '/resource/photo/test.jpg',
                'description': '''
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
                Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
                sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
                proident.
                '''
            },
            {
                'name': 'Test4',
                'school': 'Test University',
                'GPA': 3.67,
                'tel': '13233333333',
                'we_chat': 'test123',
                'photo': '/resource/photo/test.jpg',
                'description': '''
                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry
                richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch.
                Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor,
                sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et.
                Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea
                proident.
                '''
            }
        ]
