from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit', views.stu_edit),
    url(r'^main', views.main_page),
    url(r'^login',views.stu_login),
    url(r'^register',views.stu_register),
    url(r'^select',views.select_teacher),
]