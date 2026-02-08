from django import forms
from django.core.exceptions import ValidationError

from contact import models

class ContactForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Não usar ao mesmo tempo em outro lugar
        # self.fields['first_name'].widget.attrs.update({
        #     'class':'class-a class-b',
        #     'placeholder':'Escreva seu nome.'
        # })

    class Meta:
        model = models.Contact
        fields = 'first_name','last_name','phone',
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'class a class b',
        #             'placeholder': 'Seu nome'
        #         }
        #     )
        # }


    def clean(self):
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name', ValidationError(
                'Nome inválido', code='invalid'
            )
        )
