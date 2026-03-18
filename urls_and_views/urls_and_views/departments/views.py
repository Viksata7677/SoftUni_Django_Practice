from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hello!')


def view_with_name(request, variable):
    return HttpResponse(f"<h1>Variable: {variable}</h1>")