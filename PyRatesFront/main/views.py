from django.shortcuts import render, redirect
from .forms import UserSignUpForm, SelectionForm


def Home(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Filter)
    context = {'form': form}
    return render(request, 'main/home.html', context)


def Filter(request):
    # run algorithm to select a profile to display

    form = SelectionForm()
    if request.method == 'POST':
        form = SelectionForm(request.POST)
        if form.is_valid():
            # add form response to text file
            print(request.POST)
        return redirect(Filter)
    context = {'form': form}
    return render(request, 'main/filter.html', context)
