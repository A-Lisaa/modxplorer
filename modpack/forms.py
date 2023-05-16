from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from . import models


class ModModelForm(BSModalModelForm):
    class Meta:
        model = models.Mod
        fields = ["link", "name", "description", "category", "tags"]

class ModpackModelForm(BSModalModelForm):
    class Meta:
        model = models.Modpack
        fields = ["name", "description"]
