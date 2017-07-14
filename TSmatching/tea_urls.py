from django.conf.urls import url
from . import tea_views

urlpatterns = [
    url('^$', tea_views.login, name='tea_login_page')
]