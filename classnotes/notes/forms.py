from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note

class RegisterForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

CATEGORY_CHOICES = [
    ("General", "General"),
    ("Math", "Math"),
    ("CS", "CS"),
    ("Physics", "Physics"),
    ("Other", "Other"),
]

class NoteForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Note
        fields = ["title", "url", "category", "start_date", "due_date", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g., Advanced Calculus Tutorial"}),
            "url": forms.URLInput(attrs={"placeholder": "https://example.com"}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "content": forms.Textarea(attrs={"placeholder": "Brief description of the resource"}),
             "due_date": forms.DateInput(attrs={"type": "date"}),
        }
