from django import forms

class LonginForm(forms.Form):
    name=forms.CharField()
    