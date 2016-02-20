from django.conf.urls import url

from . import views

app_name = 'socialtodo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/register/$', views.user_register, name='user_register'),
    url(r'^user/login/$', views.user_login, name='user_login'),
    url(r'^user/logout/$', views.user_logout, name='user_logout'),
    url(r'^task/create/$', views.task_create, name='task_create'),
    url(r'^task/toggle$', views.task_complete, name='task_complete'),
    url(r'^task/delete$', views.task_delete, name='task_delete'),

]