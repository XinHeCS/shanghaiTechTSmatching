from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .model.forms import RegisterForm, LoginForm, EditForm
from .model.models import Students, Teachers, Selection


# Log student in.
def stu_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get user name and password
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']

            user = authenticate(username=user_name, password=user_pwd)
            print(user)
                # check the login info
                # if failed, jump to the register page
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('stu_main'))
            else:
                return render(request, 'students/stu_login.html',{'form': form, 'can_not_login' : True})
        else:
            return render(request, 'students/stu_login.html', {'form': form, 'can_not_login': True})
    form = LoginForm()
    return render(request, 'students/stu_login.html', {'form': form, 'can_not_login': False})

def stu_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and form.cleaned_data['user_pwd'] == form.cleaned_data['user_pwd_confirm']:
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['user_pwd']
            email = form.cleaned_data['user_email']
            user = User.objects.create_user(user_name,"",password)
            #create an entry in student which connected with auth table
            stu = Students(user_name=user_name,email=email)
            stu.save()
            return HttpResponseRedirect('./login')
        else:
            return render(request, 'students/stu_register.html', {'form' : form,'err' : '请检查用户名密码是否符合要求'})
    else:
        form = RegisterForm()
    return render(request, 'students/stu_register.html', {'form':form})
#show current user's profile
@login_required(login_url='/student/login/', redirect_field_name = None)
def main_page(request):
    #Students.objects.get_or_create(user_name=request.user.username)
    stu_profile = Students.objects.get(user_name=request.user.username)
    return render(request, 'students/main_page.html',{'name':request.user.username, 'stu':stu_profile})

@login_required(login_url='/student/login/', redirect_field_name = None)
def stu_edit(request):
    form = EditForm()
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        form.encoding = 'utf-8'
        print(form.is_valid())
        if form.is_valid():
            stu = Students.objects.get(user_name=request.user.username)
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
            stu.attachment = form.cleaned_data['stu_attachment']
            stu.sex = form.cleaned_data['stu_sex']
            stu.photo = form.cleaned_data['stu_pic']
            stu.save()
            return render(request, 'students/stu_edit.html', {'form': form})
    return render(request, 'students/stu_edit.html', {'form':form})

@login_required(login_url='/student/login/', redirect_field_name = None)
def select_teacher(request):
    #t = Teachers()
    #t.spider()
    #t.save_spider_data()
    t_list = Teachers.objects.all()
    if Selection.objects.filter(student_id=request.user.username).count() == 0:
        Selection.objects.create(student_id=request.user.username)

    stu_selection = Selection.objects.get(student_id=request.user.username)
    try:
        s1 = Teachers.objects.get(id=stu_selection.first_id).name
        s2 = Teachers.objects.get(id=stu_selection.second_id).name
        s3 = Teachers.objects.get(id=stu_selection.third_id).name
    except Exception:
        s1,s2,s3 = "尚未选择", "尚未选择", "尚未选择"
    if request.method == "POST":
        selection1 = int(request.POST.get('t1'))+1
        selection2 = int(request.POST.get('t2'))+1
        selection3 = int(request.POST.get('t3'))+1
        stu_selection.first_id = selection1
        stu_selection.second_id = selection2
        stu_selection.third_id = selection3
        stu_selection.save()
        s1 = Teachers.objects.get(id=stu_selection.first_id).name
        s2 = Teachers.objects.get(id=stu_selection.second_id).name
        s3 = Teachers.objects.get(id=stu_selection.third_id).name
    return render(request, 'students/teacher_selection.html', {'info':t_list,
                                                               'first_teacher':s1,
                                                               'second_teacher': s2,
                                                               'third_teacher': s3
                                                               })

def log_out(request):
    logout(request)
    return HttpResponseRedirect('./login')

# class AutoUpdate(UpdateView):
#     model = Students
#     template_name_suffix = '_update_form'
#     success_url = '/student/edit'
#     form_class = EditForm
#
#     def get_form_kwargs(self):
#         kwargs = super(AutoUpdate, self).get_form_kwargs()
#         kwargs.update({
#             'user_name': self.request.user
#         })
#         return kwargs