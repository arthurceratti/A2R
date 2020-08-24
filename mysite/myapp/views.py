from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Empresa
from .forms import MyForm

# Create your views here.

def index(request): # < here
    return render(request, 'myapp/index.html')

def detail(request):
    empresas = Empresa.objects.all()
    return render(request, 'myapp/detail.html', {'empresas': empresas })
    #return render(request, 'myapp/detail.html')

def create(request): # < here
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
        return render(request, 'myapp/edit.html', {'form': form })


    
