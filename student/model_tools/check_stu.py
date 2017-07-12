from ..models import Students

class StudentValidator(Students):
    # test function
    def can_login(self, user_name, user_pwd):
        return True

