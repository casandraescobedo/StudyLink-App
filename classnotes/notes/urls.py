from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list, name="notes_list"),
    path("notes/new/", views.note_create, name="note_create"),
    path("notes/edit/<int:pk>/", views.note_edit, name="note_edit"),
    path("notes/delete/<int:pk>/", views.note_delete, name="note_delete"),
]
