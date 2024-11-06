from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titles = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)  # Corregido aquí
    published_date = models.DateTimeField(blank=True, null=True)  # Corregido aquí

    def publishs(self):
        self.published_date = timezone.now()  # Asegúrate de guardar la fecha publicada
        self.save()

    def __str__(self):
        return self.titles  # Cambiado a 'titles'

