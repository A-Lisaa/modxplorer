from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.views.generic.edit import DeleteView

from . import forms, models


@login_required
@require_GET
def empty(request: HttpRequest) -> HttpResponse:
    return render(request, "modpack/empty.html")


@login_required
@require_GET
def home(request: HttpRequest, pk: str) -> HttpResponse:
    modpack = get_object_or_404(models.Modpack, pk=pk)
    if not (request.user == modpack.owner or request.user in modpack.collaborators.all()):
        return render(request, "modpack/alert.html", {'alert': "You don't have access to this modpack"})
    return render(request, "modpack/home.html", {'modpack': modpack})


@login_required
@require_GET
def content(request: HttpRequest, pk: int) -> HttpResponse:
    modpack = models.Modpack.objects.get(pk=pk)
    data = {
        "content_list": render_to_string(
            "modpack/content.html",
            {
                "folders": modpack.subfolders.all(),
                "mods": modpack.submods.all()
            },
            request
        )
    }
    return JsonResponse(data)


@login_required
@require_GET
def current_user_modpacks(request: HttpRequest) -> HttpResponse:
    modpacks = models.Modpack.objects.all().filter(owner=request.user)
    data = {
        "modpacks": render_to_string(
            "modpack/modpacks.html",
            {"modpacks": modpacks},
            request
        )
    }
    return JsonResponse(data)


def is_ajax(request: HttpRequest) -> bool:
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_model_by_name(model_name: str, model_pk: int):
    model_type = getattr(globals()["models"], model_name)
    model = model_type.objects.get(pk=model_pk)
    return model


class ModCreateView(BSModalCreateView):
    template_name = "modpack/forms/create_mod.html"
    form_class = forms.ModModelForm
    success_message = "Mod created successfully"

    def form_valid(self, form: forms.ModModelForm):
        if is_ajax(self.request):
            form.instance.save()

            parent = get_model_by_name(self.kwargs['parent_type'], self.kwargs['parent_pk'])
            parent.submods.add(form.instance)

        # asyncUpdate doesn't work
        #return HttpResponse(status=204)
        return redirect(self.request.headers.get('Referer'))


class ModUpdateView(BSModalUpdateView):
    model = models.Mod
    template_name = 'modpack/forms/update_mod.html'
    form_class = forms.ModModelForm
    success_message = 'Mod updated successfully'

    def form_valid(self, form: forms.ModModelForm):
        if is_ajax(self.request):
            form.instance.save()

        return HttpResponse(status=204)


class ModDeleteView(DeleteView):
    model = models.Mod
    template_name = 'modpack/forms/delete_mod.html'
    success_message = 'Mod deleted successfully'

    def form_valid(self, _):
        self.get_object().delete()

        return HttpResponse(status=204)


class FolderCreateView(BSModalCreateView):
    template_name = "modpack/forms/create_folder.html"
    form_class = forms.FolderModelForm
    success_message = "Folder created successfully"

    def form_valid(self, form: forms.FolderModelForm):
        if is_ajax(self.request):
            form.instance.save()

            parent = get_model_by_name(self.kwargs['parent_type'], self.kwargs['parent_pk'])
            parent.subfolders.add(form.instance)

        # asyncUpdate doesn't work
        #return HttpResponse(status=204)
        return redirect(self.request.headers.get('Referer'))


class ModpackCreateView(BSModalCreateView):
    template_name = "modpack/forms/create_modpack.html"
    form_class = forms.ModpackModelForm
    success_message = "Modpack created successfully"
    success_url = "dummy"

    def form_valid(self, form: forms.ModpackModelForm):
        form.instance.owner = self.request.user
        super().form_valid(form)
        success_url = reverse('modpack:home', kwargs={"pk": form.instance.pk})
        return redirect(success_url)
