from django.contrib import admin
from .models import Course, StepCourse, ContentCourse

# Register your models here.
class CoursePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class CourseStepAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class ContentCourseAdmin(admin.ModelAdmin):
    list_display = ('step','title')

admin.site.register(Course,        CoursePageAdmin)
admin.site.register(StepCourse,    CourseStepAdmin)
admin.site.register(ContentCourse, ContentCourseAdmin)
