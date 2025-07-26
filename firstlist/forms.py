from django import forms
from .models import DefaultLink

class DefaultLinkForm(forms.ModelForm):
    class Meta:
        model = DefaultLink
        fields = ["original_link"]
        widgets = {"url" : forms.Textarea}

class DefaultLinkFormGet(forms.ModelForm):
    class Meta:
        model = DefaultLink
        fields = ["shortlink"]
        widgets = {"url" : forms.Textarea}
