from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET, require_http_methods

from . import forms

User = get_user_model()


class CustomLogoutView(LogoutView):
    redirect_to = reverse_lazy("home")

@require_http_methods(['GET', 'POST'])
def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.POST.get('next', 'accounts:profile'))
    else:
        form = forms.UserCreationForm()
    return render(request, "registration/register.html", {'form': form})

@require_GET
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "registration/profile.html")
