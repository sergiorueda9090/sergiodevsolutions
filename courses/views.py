import html
from django.shortcuts import render, get_object_or_404
from .models          import Course, StepCourse, ContentCourse


# Create your views here.
def course_detail(request, course_slug, step_slug=None):
    course = get_object_or_404(Course, slug=course_slug)
    steps = course.steps.all().order_by('position')  # Obtiene todos los pasos relacionados con el curso

    step = None
    content = None

    # Si hay un step_slug, obtenemos el contenido asociado
    if step_slug:
        step = get_object_or_404(StepCourse, slug=step_slug, course=course)
        content = step.contents.all()
   
        for conten in content:
            content.recomendation = html.unescape(conten.recomendation)

    return render(request, 'course.html', {
        'course': course,
        'steps': steps,
        'step': step,
        'contents': content,
        'step_slug': step_slug  # Pasamos step_slug al contexto
    })