from django.shortcuts import render, redirect
from .forms import UserSignUpForm, SelectionForm
from .models import UserProfileModel


def Home(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            obj = UserProfileModel()
            obj.username = form.cleaned_data['username']
            obj.location = form.cleaned_data['location']
            obj.hackathons = '; '.join(form.cleaned_data['hackathons'])
            obj.databases = '; '.join(form.cleaned_data['databases'])
            obj.progLanguages = '; '.join(form.cleaned_data['progLanguage'])
            obj.interests = '; '.join(form.cleaned_data['interests'])
            obj.save()
            return redirect(Filter, kwargs=obj.userID)
    else:
        form = UserSignUpForm()
        context = {'form': form}
        return render(request, 'main/home.html', context)


def Filter(request, profile):
    # run algorithm to select a profile to display
    matchedProfile = 'ALGO'

    form = SelectionForm()
    if request.method == 'POST':
        form = SelectionForm(request.POST)
        if form.is_valid():
            # run the results optimization algorithm
            data = [matchedProfile, profile, form.cleaned_data['Match?']]
        return redirect(Filter)

    context = {'form': form}
    return render(request, 'main/filter.html', context)
