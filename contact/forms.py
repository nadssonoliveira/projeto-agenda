from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from contact import models

class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'classe-a classse-b',
                'placeholder': 'first name'
            }
            ),
            label='Primeiro Nome',
            help_text='Texto para ajudar o usuário',
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'classe-a classse-b',
                'placeholder': 'last name'
            }
            ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'your phone'
            }
        )
    )    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'youremail@example.com'
            }
        )
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Não usar ao mesmo tempo em outro lugar
        # self.fields['first_name'].widget.attrs.update({
        #     'class':'class-a class-b',
        #     'placeholder':'Escreva seu nome.'
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone',
            'email', 'description', 'category', 'picture'
                  )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'class a class b',
        #             'placeholder': 'Seu nome'
        #         }
        #     )
        # }


    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name ==  last_name:
            msg = ValidationError('Primeiro nome não pode ser igual ao ultimo.', code='invalid')

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)



        return super().clean()


    def clean_first_name(self):

        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
            'first_name', ValidationError(
                'Veio do add_error', code='invalid'
            )
        )
        return first_name
    

class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
        
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg_error = ValidationError('O nome e sobrenome não podem ser iguais.', code='invalid')
            self.add_error('first_name', msg_error)
            self.add_error('last_name', msg_error)


    def clean_email(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        email_check = User.objects.filter(email=email)

        if email_check.exists():
            msg_error = ValidationError('Já existe este e-mail', code='invalid')
            self.add_error(
                'email',
                msg_error
            )

        return email
    

 