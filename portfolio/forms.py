#from django import forms
#from .models import contact

#class ContactForm(forms.ModelForm):
#    class Meta:
 #       model = contact
  #      fields = "__all__"

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
    
