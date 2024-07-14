from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['title' ,  'image' , 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }