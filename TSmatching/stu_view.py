from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .model.fetch_teacher_infomation import TeacherInformationSpider

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .model.fetch_teacher_infomation import TeacherInformationSpider
from .model.forms import RegisterForm, LoginForm, EditForm
from .model.models import Students


# Create your views here.
def stu_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get user name and password
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']
            print(user_name+user_pwd)
            user = authenticate(username=user_name, password=user_pwd)
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
            user = User.objects.create_user(user_name,"",password)
            stu = Students(user_name=user_name,email=email)
            stu.save()
            return HttpResponseRedirect('./login')
        else:
            return render(request, 'students/stu_register.html', {'form' : form,'err' : '请检查用户名密码是否符合要求'})
    else:
        form = RegisterForm()
    return render(request, 'students/stu_register.html', {'form':form})
def main_page(request):
    stu_profile = Students.objects.get(user_name=request.user.username)
    stu_profile.save()
    print(stu_profile.major)
    print(stu_profile.email)
    return render(request, 'students/main_page.html',{'name':request.user.username})

@login_required
def stu_edit(request):
    form = EditForm()
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            stu = Students.objects.get(user_name=request.user.username)
            form.encoding = 'utf-8'
            stu.resident_id = form.cleaned_data['stu_id']
            stu.name = form.cleaned_data['stu_name']
            stu.date_of_birth = form.cleaned_data['stu_birth']
            stu.email = form.cleaned_data['stu_email']
            stu.phone_number = form.cleaned_data['stu_phone_number']
            stu.university = form.cleaned_data['stu_university']
            stu.major = form.cleaned_data['stu_major']
            stu.gpa = form.cleaned_data['stu_gpa']
            stu.ranking = form.cleaned_data['stu_ranking']
            stu.comment = form.cleaned_data['stu_comment']
            #stu.attachment = EditForm.cleaned_data['stu_attachment']
            stu.save()
            return render(request, 'students/stu_edit.html', {'form': form})
    return render(request, 'students/stu_edit.html', {'form':form})

@login_required
def select_teacher(request):
    t_spider = TeacherInformationSpider()
    t_spider.spider()
    t_spider.process_data()
    t_info = t_spider.return_data()
    if request.method == "POST":
        selection1 = request.POST.get('t1')
        selection2 = request.POST.get('t2')
        selection3 = request.POST.get('t3')
        print(selection1)

        return render(request, 'students/teacher_selection.html', {'info': t_info})
    return render(request, 'students/teacher_selection.html', {'info':t_info})


