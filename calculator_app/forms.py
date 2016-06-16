from django import forms


class Calculate(forms.Form):
    operators = [('X', 'X'), ('+', '+'), ('-', '-'), ('/', '/')]
    first_number = forms.FloatField(label='Enter number ')
    operator_choice = forms.ChoiceField(operators, label='Pick operator  ',
                             required=True)
    second_number = forms.FloatField(label=' Second number ')
