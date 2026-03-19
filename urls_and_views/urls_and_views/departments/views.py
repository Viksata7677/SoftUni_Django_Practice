from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from urls_and_views.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse('Hello!')


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_int_pk(request, pk: int):
    return HttpResponse(f"<h2>Pk: {pk}</h2>")


def view_with_slug(request, slug):
    department = get_object_or_404(Department, slug=slug)
    return HttpResponse(f'<h3>Department from slug: {department}</h3>')