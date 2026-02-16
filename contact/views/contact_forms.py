from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.models import Contact
from contact import forms

# Create your views here.
def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = forms.ContactForm(request.POST, request.FILES)

        context = {
            'form': forms.ContactForm(request.POST),
            'form_action':form_action,
            'form_title':'Contact'
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
            

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': forms.ContactForm(),
        'form_action': form_action,
        'form_title':'Contact'
    }

    return render(
        request,
        'contact/create.html',
        context,
    )


def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = forms.ContactForm(request.POST,request.FILES, instance=contact)

        context = {
            'form': forms.ContactForm(request.POST),
            'form_action':form_action,
            'form_title':'Contact'
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
            

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': forms.ContactForm(instance=contact),
        'form_action': form_action,
        'form_title':'Contact'
    }

    return render(
        request,
        'contact/create.html',
        context,
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )
    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()

        return redirect('contact:index')
    return render(
        request, 'contact/contact.html', {
            'contact': contact,
            'confirmation': confirmation
        }
    )