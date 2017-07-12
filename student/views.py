from django.shortcuts import render
from django.http import HttpResponse
from .model_tools.stu_db import StudentValidator
from .forms import LoginForm, RegisterForm

# Create your views here.
def stu_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # Get user name and password
        if form.is_valid():
            stu_val = StudentValidator()
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

    return render(request, 'stu_login.html', {
        'form': form
    })





