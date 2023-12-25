from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return str(self.name)

class Folder(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=65536, default="", blank=True)

    subfolders = models.ManyToManyField("self", symmetrical=False)
    submods = models.ManyToManyField("Mod")

def get_uncategorised_category() -> Category:
    return Category.objects.get_or_create(name="Uncategorized")[0]

class Mod(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=65536, default="", blank=True)

    link = models.URLField()
    category = models.ForeignKey(
        Category,
        models.SET(get_uncategorised_category),
        default=get_uncategorised_category
    )
    tags = models.ManyToManyField("Tag", blank=True)
    requirements = models.ManyToManyField("self")

    subfolders = models.ManyToManyField("Folder")
    submods = models.ManyToManyField("self", symmetrical=False)


class Modpack(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=65536, default="", blank=True)

    subfolders = models.ManyToManyField("Folder")
    submods = models.ManyToManyField("Mod")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="collaborators")
