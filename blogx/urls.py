from django.contrib import admin
from django.urls import path,include
from blogx.views import UserRegistrationView, UserLoginView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('passwordreset/', SendPasswordResetEmailView.as_view(), name='passwordreset'),
     path('resetpassword/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]