from django.shortcuts import render

from .forms import CallForm


# Create your views here.


def home(request):
    form = CallForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        form = CallForm()

    return render(request, 'home.html', {'form': form, })
