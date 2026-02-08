from django.shortcuts import render

from contact.models import Contact
from contact import forms

# Create your views here.
def create(request):

    if request.method == 'POST':
        context = {
            'form': forms.ContactForm(request.POST)
        }

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