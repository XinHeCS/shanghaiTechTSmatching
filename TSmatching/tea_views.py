from django.shortcuts import render
from .model.forms import LoginForm
from .model.utility import TeacherHandle

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # check the teacher's ID
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']
            tea_hdl = TeacherHandle(user_name, user_pwd)

            # check the login info
            # if failed, jump to the register page
            if tea_hdl.can_login():
                return render(request, 'teacher/main_page.html', {
                    'user': user_name,
                    'success_login': True,
                    'stu_info': tea_hdl.get_students()
                })
            else:
                return render(request, 'teacher/login.html', {
                    'form': form,
                    'success_login': False
                })
    else:
        form = LoginForm()
        return render(request, 'teacher/login.html', {
            'form': form,
            'success_login': True
        })
