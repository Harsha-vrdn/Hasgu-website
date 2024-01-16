from django.shortcuts import render, HttpResponse


# Create your views here.
def home(requests):
    return HttpResponse("This is Home page")
