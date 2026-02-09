from django.shortcuts import render, redirect

from contact.models import Contact
from contact import forms

# Create your views here.
def create(request):

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        context = {
            'form': forms.ContactForm(request.POST)
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:create')
            

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': forms.ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )