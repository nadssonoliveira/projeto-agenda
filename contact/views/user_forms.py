from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm

from contact import forms

def register(request):
    form = forms.RegisterForm()
   

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')
    

    context = {
        'form_title':'Register',
        'form': form
    }
    return render(request, 'contact/register.html', context)

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            print(user)

    return render(request, 'contact/login.html', {
        'form': form
    })