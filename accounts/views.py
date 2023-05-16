from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods


class CustomLoginView(LoginView):
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        response = super().form_invalid(form)
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        print(next_url)
        print(f"{self.request.path}?next={next_url}")
        if next_url:
            return redirect(f"{self.request.path}?next={next_url}")
        return response

@require_http_methods(['GET', 'POST'])
def register(request: HttpRequest) -> HttpResponse:
    print(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            next_url = request.POST.get('next')
            print(next_url)
            if next_url is not None:
                print(next_url)
                return redirect(next_url)
            return redirect('accounts:profile')
        return render(request, "registration/register.html", {'form': form})
    form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})

@require_GET
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "registration/profile.html")
