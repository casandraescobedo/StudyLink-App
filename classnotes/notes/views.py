from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

from .models import Note
from .forms import RegisterForm, NoteForm


def register(request):
    if request.user.is_authenticated:
        return redirect("notes_list")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("notes_list")
    else:
        form = RegisterForm()

    return render(request, "notes/register.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def notes_list(request):
    filter_type = request.GET.get("filter", "all")  # all | mine | public

    if filter_type == "mine":
        notes = Note.objects.filter(owner=request.user)
    elif filter_type == "public":
        notes = Note.objects.filter(is_public=True)
    else:
        notes = Note.objects.filter(
            Q(owner=request.user) | Q(is_public=True)
        ).distinct()

    total_notes = notes.count()
    categories_count = notes.values("category").distinct().count()

    start_week = timezone.now() - timedelta(days=7)
    this_week_count = notes.filter(created_at__gte=start_week).count()

    return render(
        request,
        "notes/notes_list.html",
        {
            "notes": notes,
            "total_notes": total_notes,
            "categories_count": categories_count,
            "this_week_count": this_week_count,
            "active_filter": filter_type,   # ⭐ tell template which tab is active
        },
    )


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("notes_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)  # owner-only

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.owner = request.user  # keep ownership locked
            updated.save()
            return redirect("notes_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form, "is_edit": True})


@login_required
@require_POST
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    note.delete()
    return redirect("notes_list")

