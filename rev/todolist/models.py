from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Todo(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    due = models.DateTimeField(blank=True)
