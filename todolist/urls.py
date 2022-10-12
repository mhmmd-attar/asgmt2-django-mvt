from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('create-task/', create_task, name='create_task'), 
    path('finished/<int:id>', finished_status, name='finished'),
    path('delete/<int:id>', delete_task, name='delete'), 
    path('json/', todolist_json, name='json'),
    path('ajax/', show_todolist_ajax, name='ajax'),
    path('update/<int:id>', update_ajax, name='update_ajax'),
    path('dlt/<int:id>', delete_ajax, name='delete_ajax'),
    path('add/', add_task, name='add_task')
]