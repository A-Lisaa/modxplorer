from bootstrap_modal_forms.forms import BSModalModelForm

from . import models


class ModModelForm(BSModalModelForm):
    class Meta:
        model = models.Mod
        fields = ["link", "name", "description", "category", "tags"]

class FolderModelForm(BSModalModelForm):
    class Meta:
        model = models.Folder
        fields = ["name", "description"]

class ModpackModelForm(BSModalModelForm):
    class Meta:
        model = models.Modpack
        fields = ["name", "description"]
