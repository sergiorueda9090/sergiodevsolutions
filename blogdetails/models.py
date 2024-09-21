from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.
class DetailPage(models.Model):
    title            = models.CharField(max_length=255)
    slug             = models.SlugField(max_length=255, unique=True, blank=True)
    image            = models.ImageField(upload_to='images/')
    subTile          = models.TextField()
    myDescription    = models.TextField()
    imageDescription = models.ImageField(upload_to='images/')
    titleBenefits    = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogdetails:blog_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

class BenefitsPage(models.Model):
    detail_page = models.ForeignKey(DetailPage, on_delete=models.CASCADE, related_name='benefits')
    description = HTMLField()

    def __str__(self):
        return self.description
    
class ServicesPage(models.Model):
    detail_page = models.ForeignKey(DetailPage, on_delete=models.CASCADE, related_name='services')
    description = HTMLField()

    def __str__(self):
        return self.description
