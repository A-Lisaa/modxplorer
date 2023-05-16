import uuid

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
    folders = models.ManyToManyField("self")
    mods = models.ManyToManyField("Mod")

def get_uncategorised_category() -> Category:
    return Category.objects.get_or_create(name="Uncategorized")[0]

class Mod(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=65536, default="", blank=True)
    category = models.ForeignKey(
        Category,
        models.SET(get_uncategorised_category),
        default=get_uncategorised_category
    )
    tags = models.ManyToManyField(Tag, blank=True)
    mods = models.ManyToManyField("self")

class Modpack(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=65536, default="", blank=True)
    folders = models.ManyToManyField("self")
    mods = models.ManyToManyField("Mod")
