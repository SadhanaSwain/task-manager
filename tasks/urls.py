from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),        # 👈 This makes dashboard default
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('analytics/', views.analytics_dashboard, name='analytics'),
    path('toggle_complete/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
]