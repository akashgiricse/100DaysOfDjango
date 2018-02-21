from django.conf.urls import url
from . import views

urlpatterns = [
    # post view
    url(r'^login/$', views.user_login, name='login'),

]
