from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserLogoutView  ,TaskManagementView


urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('auth/login/', UserLoginView.as_view(), name='user-login'),
    path('auth/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('task/', TaskManagementView.as_view(), name='task'),
    path('task/<int:task_id>/', TaskManagementView.as_view(), name='task-id'),
]
