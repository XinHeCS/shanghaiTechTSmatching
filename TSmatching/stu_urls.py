from django.conf.urls import url 
from . import stu_view

urlpatterns = [
    url(r'^edit', stu_view.stu_edit, name='stu_edit'),
    url(r'^main', stu_view.main_page, name='stu_main'),
    url(r'^login',stu_view.stu_login, name='stu_login'),
    url(r'^register',stu_view.stu_register, name='stu_register'),
    url(r'^select',stu_view.select_teacher, name='stu_select')
]