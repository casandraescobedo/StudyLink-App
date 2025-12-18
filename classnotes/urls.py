from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from notes import views as notes_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("register/", notes_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="notes/login.html"), name="login"),
    path("logout/", notes_views.logout_view, name="logout"),

    # Notes app routes live inside notes/urls.py
    path("", include("notes.urls")),
]
