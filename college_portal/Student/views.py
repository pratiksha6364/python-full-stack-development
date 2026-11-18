
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table

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

def forms(request):
    if request.method == "POST":
        regno = request.POST.get('regno')
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        email = request.POST.get('email')
        dob = request.POST.get('dob')

        Student_table.objects.create(
            regno=regno,
            name=name,
            marks=marks,
            email=email,
            dob=dob
        )

        return render(request, 'studentform.html', {
            'message': 'Saved successfully!'
        })

    return render(request, 'studentform.html')