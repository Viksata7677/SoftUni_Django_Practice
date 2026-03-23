from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forum_app.posts.forms import PersonForm, PostBaseForm
from forum_app.posts.models import Post


# Create your views here.


def index(request):

    form = PersonForm(request.POST or None)

    if request.method == "POST":
        print(request.POST['person_name'])

        if form.is_valid():
            print(form.cleaned_data['person_name'])

    context = {
        'my_form': PersonForm(),
    }

    return render(request, 'base.html', context=context)


def dashboard(request):
    content = {
        'posts': Post.objects.all()
    }

    return render(request, 'posts/dashboard.html', content)


def add_post(request):
    form = PostBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'posts/add-post.html', context)