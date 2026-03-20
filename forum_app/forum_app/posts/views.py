from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        'current_time': datetime.now(),
        'person': {
            'age': 20,
            'height': 190
        },
        'ids': ['123', '321'],
        'text': 'Hello my name is Viktor!',
        'users': ['Viktor', 'Aleks', 'Ivan']
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