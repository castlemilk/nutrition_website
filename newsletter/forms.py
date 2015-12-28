from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        #exclude = ['full_name']


    def clean_email(self):
        #print self.cleaned_data
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension  = provider.split('.')
        if extension != 'edu':
            raise forms.ValidationError("Please enter a valid .edu address")
        return email

    def clean_full_name(self):
        #print self.cleaned_data
        full_name = self.cleaned_data.get('full_name')
        #print full_name
        return full_name


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()
