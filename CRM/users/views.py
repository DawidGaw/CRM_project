from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from .models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages

class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            messages.success(request, f"Account created for {user.username}! You can now log in.")
            return redirect('login')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.role == 'admin':
            print("Admin access")
        elif request.user.role == 'sales':
            print("Sales access")
        elif request.user.role == 'support':
            print("Support access")

        return super().get(request, *args, **kwargs)