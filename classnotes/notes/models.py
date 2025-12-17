from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    title = models.CharField(max_length=200)

    url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, default="General")

    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    content = models.TextField(blank=True)  # description (optional)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
