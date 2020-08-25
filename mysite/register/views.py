from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST) #classe default era UserCreationForm, porém foi definida uma nova classe em forms.py, agora chamada de RegisterForm
        if form.is_valid():
            form.save()
        return redirect("/") # local para onde o usuário é redirecionado depois de criar seu registro
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})