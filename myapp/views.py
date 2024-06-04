import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def my_view(request):
    api_url = 'https://restcountries.com/v3.1/all'

    # Make a request to the API and get the response
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the response to a format that Python can understand
        countries = response.json()
    else:
        # Handle the case where the request was not successful
        countries = []  # Provide an empty list if there's an issue

    # Pass the retrieved data to the template
    return render(request, 'myapp/my_template.html', {'countries': countries})
