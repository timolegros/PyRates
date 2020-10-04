from django import forms
from .models import UserProfileModel


class UserSignUpForm(forms.Form):
    progLanguageChoices = (('C', 'C'), ('Python', 'Python'), ('Javascript', 'Javascript'), ('Java', 'Java'),
                           ('C#', 'C#'), ('C++', 'C++'))
    databaseChoices = (('SQL', 'SQL'), ('MongoDB', 'MongoDB'), ('Firebase', 'Firebase'), ('Oracle', 'Oracle'),
                       ('Redis', 'Redis'))
    areaOfInterestChoices = (("Web Development", "Web Development"), ("AI", "AI"),
                             ("Product Management", "Product Management"), ("Big data", "Big data"))
    hackathonChoices = ((0, '0'), (1, '1-3'), (2, '4-6'), (3, '6-10'), (4, '>10'))
    locationChoices = (("East Coast", "East Coast"), ("Midwest", "Midwest"), ("West Coast", "West Coast"),
                       ("Southern US", "Southern US"), ("Northern US", "Northern US"),
                       ("Eastern Canada", "Eastern Canada"), ("Western Canada", "Western Canada"),
                       ("Atlantic Provinces", "Atlantic Provinces"), ("Outside US/ Canada", "Outside US/ Canada"))

    username = forms.CharField(label='Username', max_length=30, required=True)
    location = forms.ChoiceField(label='Location', choices=locationChoices, required=True)
    hackathons = forms.ChoiceField(label='Number of hackathons attended', choices=hackathonChoices, required=True)

    # hackathons = forms.CheckboxSelectMultiple(choices=hackathonChoices)
    databases = forms.MultipleChoiceField(label='Databases', choices=databaseChoices, required=True)
    progLanguage = forms.MultipleChoiceField(label='Programming Languages', choices=progLanguageChoices, required=True)
    interests = forms.MultipleChoiceField(label='Interests', choices=areaOfInterestChoices, required=True)


class SelectionForm(forms.Form):
    # how to make yes or now without submit button
    bool = (('1', 'Yes'), ('0', 'No'))
    YesNo = forms.ChoiceField(label='Match?', choices=bool, required=True)