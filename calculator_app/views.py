from django.shortcuts import render

from calculator_app.forms import Calculate

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
