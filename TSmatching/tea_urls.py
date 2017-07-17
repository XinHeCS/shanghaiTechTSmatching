from django.conf.urls import url
from . import tea_views

urlpatterns = [
    url(r'^login/$', tea_views.login, name='tea_login_page'),
    url(r'^messages/(accept|reject|reject_ac)/(\w+)/$', tea_views.message_page, name='tea_mess_page')
]