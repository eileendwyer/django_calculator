from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from calculator_app.forms import Calculate
from calculator_app.models import Operation


def calculate_view(request):
    result = ""
    first_number = 'Number'
    operator_choice = ''
    second_number = 'Second number'
    print(request.POST)
    if request.method == 'POST':
        form = Calculate(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data['first_number']
            second_number = form.cleaned_data['second_number']
            operator_choice = form.cleaned_data['operator_choice']
            if operator_choice == "X":
                result = first_number * second_number
            elif operator_choice == "+":
                result = first_number + second_number
            elif operator_choice == "-":
                result = first_number - second_number
            elif operator_choice == "/":
                result = first_number/second_number
                result  = form.cleaned_data
    return render(request, 'calculator.html', {'form': Calculate, 'result': result,
                                                'first': first_number, 'second': second_number,
                                                'operator_choice': operator_choice})


def index_view(request):
    form = AuthenticationForm()
    AuthenticationForm
    return render(request, "index.html", {"form": form})


@login_required
def login_view(request):
    print(request.user.password)
    return render(request, "login.html")


def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("log_view"))
        else:
            return render(request, "user_create.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create.html", {"form": form})
