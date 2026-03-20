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
        'text': 'Hello my name is Viktor!'
    }

    return render(request, 'base.html', context=context)