from django import forms
from testapp.models import Movie

class MovieForm(forms.ModelForm):
    rdate=forms.DateField()
    moviename=forms.CharField(max_length=30)
    hero=forms.CharField(max_length=30)
    heroine=forms.CharField(max_length=30)
    rating=forms.IntegerField()
    class Meta:
        model=Movie
        fields='__all__'