from django import forms


class TestForm(forms.Form):
    file = forms.FileField()