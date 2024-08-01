from django.urls import path

from accounts.views import login_view, register_view, logout_view, username_update, user_email_update, user_profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/temps/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/temps/password_change_done.html'),
         name='password_change_done'),
    path('username_update/', username_update, name='username_update'),
    path('user_email_update/', user_email_update, name='user_email_update'),
    path('user_profile/', user_profile_view, name='user_profile')
]
