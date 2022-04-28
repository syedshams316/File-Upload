from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


class Document(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name
