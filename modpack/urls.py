from django.urls import path

from . import views

app_name = 'modpack'
urlpatterns = [
    path("", views.home, name="home"),
    path("mods/", views.mods, name="mods"),
    path("create-mod/", views.ModCreateView.as_view(), name="create-mod"),
    path("create-modpack/", views.ModpackCreateView.as_view(), name="create-modpack")
    # path("add-mod", views.add_mod, name="add-mod")
    # path("tag/create/", views.TagCreateView.as_view(), name="tag-create"),
    # path("tag/<int:pk>/", views.TagUpdateView.as_view(), name="tag-update"),
    # path("tag/<int:pk>/delete", views.TagDeleteView.as_view(), name="tag-delete"),
    # path("tag/<int:pk>/details", views.TagDetailsView.as_view(), name="tag-details"),
    # path("tag/list/", views.TagListView.as_view(), name="tag-list")
]
