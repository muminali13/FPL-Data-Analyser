from django.shortcuts import render, redirect
from .forms import CreateUserForm


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/my-team/")

    context = {'registerform' : form}
    return render(request, "register/register.html", context)
