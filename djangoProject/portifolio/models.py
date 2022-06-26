from django.db import models


class App(models.Model):
    name = models.CharField(max_length=255)
    url_name = models.CharField(max_length=255, unique=True)
