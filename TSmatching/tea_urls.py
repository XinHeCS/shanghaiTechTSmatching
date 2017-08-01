from django.conf.urls import url
from . import tea_views

urlpatterns = [
    url(r'^login/$', tea_views.login, name='tea_login_page'),
    url(r'^messages/(accept|reject|reject_ac)/(\w+)/$', tea_views.message_page, name='tea_mess_page'),
    url(r'^main_page/$', tea_views.main_page, name='tea_main_page'),
    url(r'^log_out/$', tea_views.logout, name='tea_logout')
]