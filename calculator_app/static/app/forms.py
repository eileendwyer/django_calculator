from django import forms


class Calculate(forms.Form):
    operators = [('*', '*'), ('+', '+'), ('-', '-'), ('/', '/')]
    first_number = forms.FloatField(label='Enter number')
    operator_choice = forms.ChoiceField(operators, label='Pick an operator',
                             required=True)
    second_number = forms.FloatField(label='Enter second number')
