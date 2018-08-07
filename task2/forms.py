from django import forms
# from rest_framework.generics import


class MyForm(forms.ModelForm):
    input = forms.CharField(widget=forms.Textarea)
    delimiter = forms.CharField(max_length=5)

