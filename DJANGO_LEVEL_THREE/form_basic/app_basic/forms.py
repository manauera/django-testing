from django import forms
from django.core import validators

def check_z(value):
    if value[0] != 'z':
        raise forms.ValidationError("Yo shits wrong, dawg")

class TestForm(forms.Form):
    name = forms.CharField(validators=[check_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Your Email Again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean = super().clean()

        email = all_clean['email']
        verify_email = all_clean['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Email must match")
