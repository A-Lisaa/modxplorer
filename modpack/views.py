from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.http import require_GET

from . import forms, models


@login_required
@require_GET
def home(request: HttpRequest) -> HttpResponse:
    modpack_id = request.GET.get("id")
    if modpack_id is None:
        return render(request, "modpack/home.html")
    modpack = models.Modpack.objects.get(id=modpack_id)
    return render(request, "modpack/home.html", {'modpack': modpack})

@require_GET
def mods(request: HttpRequest) -> HttpResponse:
    data = {}
    mods_list = models.Mod.objects.all()
    data["list"] = render_to_string(
        "modpack/mods.html",
        {
            "mods": mods_list
        },
        request
    )
    return JsonResponse(data)

class ModCreateView(BSModalCreateView):
    template_name = "modpack/create_mod.html"
    form_class = forms.ModModelForm
    success_url = reverse_lazy("modpack:home")

class ModpackCreateView(BSModalCreateView):
    template_name = "modpack/create_modpack.html"
    form_class = forms.ModpackModelForm
    success_url = reverse_lazy("modpack:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.success_url = f"{reverse_lazy('modpack:home')}?id={form.cleaned_data['id']}"
        return response
