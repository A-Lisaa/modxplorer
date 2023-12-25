from django.urls import path

from . import views

app_name = 'modpack'
urlpatterns = [
    path("", views.empty, name="empty"),
    path("<int:pk>/", views.home, name="home"),
    path("<int:pk>/content/", views.content, name="content"),
    path('current-user-modpacks/', views.current_user_modpacks, name="current-user-modpacks"),
    path("create-modpack/", views.ModpackCreateView.as_view(), name="create-modpack"),
    path("create-mod/<str:parent_type>/<str:parent_pk>/" , views.ModCreateView.as_view(), name="create-mod"),
    path("update-mod/<int:pk>", views.ModUpdateView.as_view(), name="update-mod"),
    path("delete-mod/<int:pk>", views.ModDeleteView.as_view(), name="delete-mod"),
    path("create-folder/<str:parent_type>/<str:parent_pk>/", views.FolderCreateView.as_view(), name="create-folder"),
    # path("add-mod", views.add_mod, name="add-mod")
    # path("tag/create/", views.TagCreateView.as_view(), name="tag-create"),
    # path("tag/<int:pk>/", views.TagUpdateView.as_view(), name="tag-update"),
    # path("tag/<int:pk>/delete", views.TagDeleteView.as_view(), name="tag-delete"),
    # path("tag/<int:pk>/details", views.TagDetailsView.as_view(), name="tag-details"),
    # path("tag/list/", views.TagListView.as_view(), name="tag-list")
]
