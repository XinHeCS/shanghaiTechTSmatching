from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .model_tools.db_teacher import TeacherHandle


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # check the teacher's ID
        if form.is_valid():
            stu_val = TeacherHandle()
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']

            # check the login info
            # if failed, jump to the register page
            if stu_val.can_login(user_name, user_pwd):
                return HttpResponse('Welcome to ShanghaiTech')
            else:
                return HttpResponse('Go back and fuck yourself!')
    else:
        form = LoginForm()

    return render(request, 'teacher/login.html', {
        'form': form
    })