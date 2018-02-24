from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, login, logout_then_login
from django.contrib.auth.views import password_change, password_change_done
urlpatterns = [
    # post view
    # url(r'^login/$', views.user_login, name='login'),
    # Login/Logout url
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # Change password url
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),


]
