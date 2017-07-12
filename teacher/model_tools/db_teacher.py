from ..models import Teachers

# This class is used for checking the teacher users
# update the data of teacher in the database
class TeacherHandle:
    # check the pwd of a teacher
    def can_login(self, name, pwd):
        try:
            result = Teachers.objects.filter(name=name)
            if not result:
                return False
            else:
                return name == result[0]['phone_number']
        except Teachers.DoesNotExist:
            return False