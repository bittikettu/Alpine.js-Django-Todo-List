from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/balance', views.user_balance, name='user_balance'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/update/', views.update_task_status, name='update_task')
]