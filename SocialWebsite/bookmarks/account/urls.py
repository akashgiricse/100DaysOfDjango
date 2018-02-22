from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, login, logout_then_login

urlpatterns = [
    # post view
    # url(r'^login/$', views.user_login, name='login'),
    # Login/Logout url
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),

]
