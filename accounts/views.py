from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from accounts.forms import LoginForm, RegisterForm, UsernameUpdateForm, UserEmailUpdateForm
from anime_app.models import Favorites


# Create your views here.
# class LoginView(TemplateView):
#     template_name = 'accounts/temps/login.html'
#     form_class = LoginForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = LoginForm
#         return context


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('anime_list')
                    else:
                        messages.error(request, 'disabled account')
                        return redirect('login')
            else:
                messages.error(request, 'invalid username or password')
                return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'accounts/temps/login.html', {'form': form})
    return redirect('anime_list')


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return redirect('login')
            else:
                messages.error(request, 'error password')
        form = RegisterForm()
        return render(request, 'accounts/temps/register.html', {'form': form})
    return redirect('login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('anime_list')


@login_required
def username_update(request):
    if request.method == 'POST':
        form = UsernameUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    form = UsernameUpdateForm(instance=request.user)
    return render(request, 'accounts/temps/username_update.html', {'form': form})


@login_required
def user_email_update(request):
    if request.method == 'POST':
        form = UserEmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    form = UserEmailUpdateForm(instance=request.user)
    return render(request, 'accounts/temps/user_email_update.html', {'form': form})


@login_required
def user_profile_view(request):
    user = request.user
    favorite = Favorites.objects.filter(user=request.user)
    is_social_user = UserSocialAuth.objects.filter(user=user).exists()
    return render(request, 'accounts/temps/profile.html', {'user': request.user, 'is_social_user': is_social_user,
                                                           'favorite': favorite})

