from django import forms


class makeNameForm(forms.Form):
    makename = forms.CharField(max_length=100)