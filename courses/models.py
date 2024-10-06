from django.db import models
from django.utils.text import slugify
from django.urls import reverse



# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class StepCourse(models.Model):
    course = models.ForeignKey(Course, related_name='steps', on_delete=models.CASCADE)
    name   = models.CharField(max_length=200)
    slug   = models.SlugField(unique=True, blank=True, null=True)
    position = models.IntegerField(null=True, blank=True)  # Nuevo campo 'position'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(StepCourse, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ContentCourse(models.Model):
    step            = models.ForeignKey(StepCourse, related_name='contents', on_delete=models.CASCADE)
    title           = models.CharField(max_length=255)
    description     = models.TextField()
    command         = models.CharField(max_length=255,null=False)
    note            = models.CharField(max_length=255,null=False)
    result          = models.CharField(max_length=255,null=False)
    recomendation   = models.TextField()

    def __str__(self):
        return self.title
    



    