from django.shortcuts import render, redirect
from .model.forms import LoginForm
from .model.utility import TeacherHandle
from .model.models import Teachers

# A decorator
# Check for login status
def login_checked(func):
    def wrapper(request, *args, **kw):
        try:
            print('User: ' + request.session['user_id'] + '   request login ...')
            return func(request, *args, **kw)
        except KeyError:
            return redirect('tea_login_page')
    return wrapper

# Check user's password
def do_login(user, pwd):
    result = Teachers.objects.get(user_name=user)
    if pwd == result.password:
        return True
    else:
        return False

# Create your views here.
def login(request):
    # Clear the session
    request.session.clear()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        # check the teacher's ID
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_pwd = form.cleaned_data['user_pwd']

            # Save user ID session
            request.session['user_id'] = user_name

            # check the login info
            # if failed, jump to the register page
            if do_login(user_name, user_pwd):
                return redirect('/teacher/main_page')
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

@login_checked
def main_page(request):
    tea_hdl = TeacherHandle(request.session['user_id'])
    # Check for change password request
    change_pwd_box = {
        'form': tea_hdl.get_password_form(),
        "status": True,
        'err': ''
    }
    if request.method == 'POST':
        change_pwd_box['status'], change_pwd_box['err'] = \
            tea_hdl.try_change_password(request.POST)
    return render(request, 'teacher/main_page.html', {
        'user': tea_hdl.__str__(),
        'stu_info': tea_hdl.get_students(),
        'ac_stu_info': tea_hdl.get_accepted_students(),
        'change_password': change_pwd_box
    })

@login_checked
def message_page(request, action, stu):
    tea_hdl = TeacherHandle(request.session['user_id'])

    # check actions
    if action == 'accept':
        tea_hdl.accept(stu)
        return redirect('/teacher/main_page')
    else:
        tea_hdl.reject(stu, action)
        return redirect('/teacher/main_page')

@login_checked
def logout(request):
    request.session.clear()

    return redirect('tea_login_page')


# Change user's password
# This method will check the original password and
# change a new password for the user
# def change_password(request):
#     global tea_hdl
#
#     # Check login status
#     if not tea_hdl.can_login():
#         return redirect('tea_login_page')
#
#     # Deal with POST request
#     if request.method == 'POST':
#         status, mess = tea_hdl.try_change_password(request.POST)
#
#     # if not POST request
#     # load the page directly
#     else:
#         return redirect('tea_main_page')