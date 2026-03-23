from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from forum_app.posts.forms import PersonForm


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
        'posts': [
            {
                'title': "This is Viktor's post 1",
                'author': 'Viktor Iordanov',
                'created_at': datetime.now()
            },
            {
                'title': "This is Viktor's post 2",
                'author': 'Viktor Iordanov',
                'created_at': datetime.now()
            }
        ]
    }

    return render(request, 'posts/dashboard.html', content)