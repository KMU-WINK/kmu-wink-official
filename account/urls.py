from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.members, name='members'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:id>', views.profile, name='profile'),
    path('emoji/', views.emoji),
]

