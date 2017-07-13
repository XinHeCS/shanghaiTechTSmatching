from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .model_tools.stu_db import StudentValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import RegisterForm, LoginForm, EditForm

from django.http import HttpResponse


# Create your views here.
def stu_login(request):
    if request.method == 'POST':


        # Get user name and password
        try:
            stu_val = StudentValidator()
            user_name = request.POST['user_name']
            user_pwd = request.POST['user_pwd']


            # check the login info
            # if failed, jump to the register page
            if stu_val.can_login(user_name, user_pwd):
                return HttpResponseRedirect(request,'students/main_page.html')
            else:
                return HttpResponse('Go back and fuck yourself!')
        except:
            print('ERROR')
        return render(request, 'students/stu_login.html')



def stu_register(request):
    stu_val = StudentValidator()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and form.cleaned_data['user_pwd'] == form.cleaned_data['user_pwd_confirm']:
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['user_pwd']
            user = User.objects.create_user(user_name, password)
        else:
            return render(request, 'students/stu_register.html', {'form' : form,'err' : '请检查用户名密码是否符合要求'})
    else:
        form = RegisterForm()
    return render(request, 'students/stu_register.html', {'form':form})
def main_page(request):
    return render(request, 'students/main_page.html')

def stu_edit(request):
    form = EditForm()
    return render(request, 'students/stu_edit.html', {'form':form})



