from django import forms
from .models import Post
# from django.forms import formsets
# from django.forms.forms import Form
# from django.forms.formsets import formset_factory 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'title_tag' , 'author' , 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter title for your Blog :)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'title_tag' , 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Enter title for your Blog :)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }