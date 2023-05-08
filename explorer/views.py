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
def index(request: HttpRequest) -> HttpResponse:
    modpack_id = request.GET.get("id")
    return render(
        request,
        "explorer/modpack.html",
        {
            #"modpack": models.Modpack.objects.filter(id=modpack_id).all()
            "mods": models.Mod.objects.all()
        }
    )

@require_GET
def mods(request: HttpRequest) -> HttpResponse:
    data = {}
    mods_list = models.Mod.objects.all()
    data["list"] = render_to_string(
        "explorer/mods.html",
        {
            "mods": mods_list
        },
        request=request
    )
    return JsonResponse(data)

class ModCreateView(BSModalCreateView):
    template_name = "explorer/create_mod.html"
    form_class = forms.ModModelForm
    success_message = "Mod created successfully"
    success_url = reverse_lazy("modpack:index")
