from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('create_task/', views.create, name='create'),
    path('view_task/',views.view_task, name='view_task'),
    path('delete/', views.delete, name='delete'),
    path('update_task/<int:pk>/', views.update, name='update_task'),
    path('completed/<int:pk>/', views.completed, name='completed'),
    path('view_single_user_tasks/<int:pk>/tasks/', views.view_single_user_tasks, name='view_single_user_tasks')
]
