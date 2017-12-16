from django import forms

from account.models import*


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [""]
