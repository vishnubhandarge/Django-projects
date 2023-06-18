from django.contrib.auth.models import User
from django.db import models


class MusicFile(models.Model):
    ACCESS_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music_files/')
    access_type = models.CharField(max_length=10, choices=ACCESS_CHOICES)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    allowed_emails = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
