from ..models import Students

class StudentValidator:
    # test function
    def can_login(self, user_name, user_pwd):
        result = Students.objects.get(usr_name=user_name)
        if not result:
            return False
        else:
            return user_pwd == result[0].usr_pwd

    def can_register(self, user_name, user_pwd, user_pwd_repeat):
        return len(user_name) < 20 & user_pwd == user_pwd_repeat

class StudentEdit(Students):
    def change_basic_info(self,user, id, name, age, birthday, university, gpa, ranking, comment, email, phone, first, second, third, file):
        stu = Students.objects.get(usr_name=user)
        stu.ranking = ranking
        stu.gpa = gpa
        stu.university = university
        stu.comment = comment
        stu.email = email
        stu.phone_number = phone
        stu.age = age
        stu.date_of_birth = birthday
        stu.first_teacher = first
        stu.second_teacher = second
        stu.third_teacher = third
        stu.id = id
        stu.attachment = file
        stu.save()
    def change_pass_word(self, user, usr_pwd):
        stu = Students.objects.get(usr_name=user)
        stu.usr_pwd = usr_pwd

    def register(self, usr, usr_pwd, Email):
        pass

