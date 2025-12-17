from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from notes import views as notes_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("register/", notes_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="notes/login.html"
    ), name="login"),
    path("logout/", notes_views.logout_view, name="logout"),

    # Notes
    path("", notes_views.notes_list, name="notes_list"),
    path("notes/new/", notes_views.note_create, name="note_create"),
    path("notes/delete/<int:pk>/", notes_views.note_delete, name="note_delete"),
]
