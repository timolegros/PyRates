from django import forms
from .models import UserProfileModel


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['username', 'progChoice', 'dbChoice', 'locChoice', 'interestChoice']


class SelectionForm(forms.Form):
    bool = (('1', 'Yes'), ('0', 'No'))
    YesNo = forms.BooleanField(required=False)

