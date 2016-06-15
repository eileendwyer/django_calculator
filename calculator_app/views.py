from django.shortcuts import render

from calculator_app.forms import Calculate

def calculate_view(request):
    result = ""
    first_number = 'Number'
    operators = ''
    second_number = 'Second number'
    print(request.POST)
    if request.method == 'POST':
        form = Calculate(request.POST)
        first_number = form.cleaned_data['first_number']
        operators = form. cleaned_data['operators']
        second_number = form.cleaned_data['second_number']
        if operators == "*":
            result = first_number * second_number
        elif operators == "+":
            result = first_number + second_number
        elif operators == "-":
            result = first_number - second_number
        else:
            result = first_number/second_number
    return render(request, 'calculator.html', {'form': Calculate, 'result': result,
                                                'first': first_number, 'second': second_number,
                                                'operators': operators})
