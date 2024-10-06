from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Lear(models.Model):
    title           = models.CharField(max_length=255)
    description     = HTMLField()
    command         = models.CharField(max_length=255,null=False)
    note            = models.CharField(max_length=255,null=False)
    result          = models.CharField(max_length=255,null=False)
    recomendation   = models.CharField(max_length=255,null=False)