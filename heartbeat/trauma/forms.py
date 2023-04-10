from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(max_length=255)