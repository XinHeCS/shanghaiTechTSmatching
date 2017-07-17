from django.shortcuts import render, redirect
from .model.forms import LoginForm
from .model.utility import TeacherHandle

tea_hdl = None

# Create your views here.
def login(request):
    global tea_hdl

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
                    'stu_info': tea_hdl.get_students(),
                    'ac_stu_info': tea_hdl.get_accepted_students()
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

def message_page(request, action, stu):
    global tea_hdl

    if not tea_hdl:
        return redirect('tea_login_page')

    # check actions
    if action == 'accept':
        success, err = tea_hdl.accept(stu)
        return render(request, 'teacher/main_page.html', {
            'user': tea_hdl.__str__(),
            'stu_info': tea_hdl.get_students(),
            'ac_stu_info': tea_hdl.get_accepted_students(),
            'success': success,
            'err': err
        })
    else:
        tea_hdl.reject(stu, action)
        return render(request, 'teacher/main_page.html', {
            'user': tea_hdl.__str__(),
            'stu_info': tea_hdl.get_students(),
            'ac_stu_info': tea_hdl.get_accepted_students()
        })
