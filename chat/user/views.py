from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'user/signin.html', {'form': form})


def signup(request):
    user_form = 0
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            login(request, new_user)
            return redirect('/')
        else:
            user_form = SignUpForm()

    return render(request, 'user/signup.html', {'user_form': user_form})


class Logout(LogoutView):
    next_page = reverse_lazy('home')
