from django.shortcuts import render

# Create your views here.

def index(request): # < here
    return render(request, 'myapp/index.html')
