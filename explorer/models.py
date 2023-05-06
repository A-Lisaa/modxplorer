from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

def get_uncategorised_category() -> Category:
    return Category.objects.get_or_create(name="Uncategorized")[0]

class Folder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=65535)
    folders = models.ManyToManyField("self")
    mods = models.ManyToManyField("Mod")

class Mod(models.Model):
    link = models.URLField()

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=65535, default="", blank=True)

    category = models.ForeignKey(
        Category,
        models.SET(get_uncategorised_category),
        default=get_uncategorised_category
    )
    tags = models.ManyToManyField(Tag)

    mods = models.ManyToManyField("self")

class Modpack(Folder):
    ...
