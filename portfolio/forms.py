'''from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"'''
    
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)