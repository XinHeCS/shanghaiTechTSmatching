from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from .forms import RegisterForm, LoginForm, EditForm
from .models import Students
from django.http import HttpResponse
from django.views.generic.edit import UpdateView


# Create your views here.
def stu_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get user name and password
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']
            print(user_name+user_pwd)
            user = authenticate(username='hexin', password='wohenshuai')
            print(user)
                # check the login info
                # if failed, jump to the register page
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('./main')
            else:
                return render(request, 'students/stu_login.html',{'form': form})
        else:
            return HttpResponse('Go back and fuck yourself!')
    else:
        form = LoginForm()
        return render(request, 'students/stu_login.html', {'form': form})




def stu_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and form.cleaned_data['user_pwd'] == form.cleaned_data['user_pwd_confirm']:
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['user_pwd']
            email = form.cleaned_data['user_email']
            print(user_name+password)
            user = User.objects.create_user(user_name,email,password)
            return render(request, 'students/stu_login.html')
        else:
            return render(request, 'students/stu_register.html', {'form' : form,'err' : '请检查用户名密码是否符合要求'})
    else:
        form = RegisterForm()
    return render(request, 'students/stu_register.html', {'form':form})
def main_page(request):
    print(request.user.major)
    return render(request, 'students/main_page.html',{'name':request.user.username})

def stu_edit(request):
    if(request.method == 'POST'):
        form = EditForm(request.POST)
        if form.is_valid():
            request.user.resident_id = EditForm.cleaned_data['stu_id']
            request.user.name = EditForm.cleaned_data['stu_name']
            request.user.date_of_birth = EditForm.cleaned_data['stu_birth']
            request.user.email = EditForm.cleaned_data['stu_email']
            request.user.phone_number = EditForm.cleaned_data['stu_phone_number']
            request.user.university = EditForm.cleaned_data['stu_university']
            request.user.major = EditForm.cleaned_data['stu_major']
            request.user.gpa = EditForm.cleaned_data['stu_gpa']
            request.user.ranking = EditForm.cleaned_data['stu_ranking']
            request.user.comment = EditForm.cleaned_data['stu_comment']
            request.user.attachment = EditForm.cleaned_data['stu_attachment']
    else:
        form = EditForm()
        return render(request, 'students/stu_edit.html', {'form': form})
    return render(request, 'students/stu_edit.html', {'form':form})



