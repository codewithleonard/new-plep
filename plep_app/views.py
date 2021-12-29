from django import forms
from django.shortcuts import redirect, render
from .forms import ClientForm

def index(request):
    return render(request, 'plep_app/index.html')

def csc320(request):
    return render(request, 'plep_app/csc320.html')

def register(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    return render(request, 'plep_app/register.html', dict(form=form))

def uid_verification(request):
    return render(request, 'plep_app/uid_verification.html')