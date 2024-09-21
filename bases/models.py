from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class HomePage(models.Model):
    image            = models.ImageField(upload_to='images/home/')
    title            = models.TextField()
    description      = models.TextField()
    slug             = models.SlugField(max_length=255, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogdetails:blog_detail', kwargs={'slug': self.slug})