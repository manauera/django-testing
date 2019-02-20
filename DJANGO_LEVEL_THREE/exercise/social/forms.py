from django import forms
from social.models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def clean(self):
        all_clean = super().clean()

        new_user = User.objects.filter(email=all_clean['email'])

        if new_user:
            raise forms.ValidationError("Email already exists")
