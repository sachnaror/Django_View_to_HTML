from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def my_view(request):
    variable1 = "Hello"
    variable2 = "Django"
    variable3 = ["orange", "mango", "lemon"]

    return render(request, 'myapp/my_template.html', {
        'variable1': variable1,
        'variable2': variable2,
        'variable3': variable3,
    })
