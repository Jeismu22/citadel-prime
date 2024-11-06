from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # Cambiado a 'title'
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)  # Corregido a 'created_date'
    published_date = models.DateTimeField(blank=True, null=True)  # Se mantiene igual

    def publish(self):  # Cambiado el nombre del método a 'publish'
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  # Cambiado a 'title' para que coincida con el campo
