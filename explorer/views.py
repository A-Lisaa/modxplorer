from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import (HttpRequest, HttpResponse, HttpResponseNotAllowed,
                         JsonResponse)
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import forms, models


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

def mods(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
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
    return HttpResponseNotAllowed(["GET"])

# def add_mod(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = forms.ModForm(request.POST)
#         if form.is_valid():
#             mod = models.Mod(**form.cleaned_data)
#             mod.save()
#         return render(request, "explorer/modpack.html", {"form": form})
#     return HttpResponseNotAllowed(["POST"])

class ModCreateView(BSModalCreateView):
    template_name = "explorer/create_mod.html"
    form_class = forms.ModModelForm
    success_message = "Mod created successfully"
    success_url = reverse_lazy("modpack:index")

# class TagCreateView(generic.edit.CreateView):
#     model = models.Tag
#     fields = ["name"]
#     success_url = reverse_lazy("explorer:tag-list")

# class TagUpdateView(generic.edit.UpdateView):
#     model = models.Tag
#     fields = ["name"]

# class TagDeleteView(generic.edit.DeleteView):
#     model = models.Tag
#     success_url = reverse_lazy("explorer:tag-list")

# class TagDetailsView(generic.DetailView):
#     model = models.Tag

# class TagListView(generic.ListView):
#     model = models.Tag
