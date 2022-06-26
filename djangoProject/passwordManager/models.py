from django.db import models
from django.urls import reverse


class Password(models.Model):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    title = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('passwordManager:detail', args=(self.pk,))

    def __str__(self):
        return self.title
