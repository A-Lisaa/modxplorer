from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from . import models


class ModModelForm(BSModalModelForm):
    class Meta:
        model = models.Mod
        fields = ["link", "name", "description"]

class ModForm(forms.ModelForm):
    class Meta:
        model = models.Mod
        fields = ["link", "name", "description"]
