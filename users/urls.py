from django.urls import path

from .views import HomeView, RegisterView, profile, ChangePasswordView

urlpatterns = [
    path('', HomeView.as_view(), name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]