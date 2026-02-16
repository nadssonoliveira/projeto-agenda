from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect

from contact import forms

def register(request):
    form = forms.RegisterForm()
   

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')
    

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
            auth.login(request, user)
            messages.success(request, f'Bem vindo, {user.first_name}!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')
    return render(request, 'contact/login.html', {
        'form': form
    })

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

@login_required(login_url='contact:login')
def user_update(request):
    form = forms.RegisterUpdateForm(instance=request.user)
    context = {
            'form': form,
            'form_title': 'Update'
        }
    if request.method != 'POST':
        return render(request, 'contact/register.html', context)
    
    form = forms.RegisterUpdateForm(data=request.POST, instance=request.user)
    context = {
            'form': form,
            'form_title': 'Update'
        }
    if not form.is_valid():
        return render(request, 'contact/register.html', context)
    
    messages.success(request, 'Update realizado com sucesso!')
    form.save()
    return redirect('contact:login')