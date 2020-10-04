from django.shortcuts import render, redirect
from .forms import UserSignUpForm


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
    return render(request, 'main/filter.html')
