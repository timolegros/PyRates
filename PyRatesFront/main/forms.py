from django import forms
from .models import UserProfileModel


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['username', 'progChoice', 'dbChoice', 'locChoice', 'interestChoice']

# class SelectionForm(forms.Form):
#     class Meta:
#         model =
#         fields =

