
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    data = {
        'name': 'abc',
        'age': 17,
        'department': 'BCA'
    }

    marks = [100, 98, 97]

    context = {
        'data': data,
        'marks': marks
    }

    return render(request, 'home.html', context)


def about(request):
    return HttpResponse("Welcome to About Page")


def contact(request):
    return HttpResponse("Welcome to Contact Page")
