#from django.shortcuts import render,redirect
#from .models import contact
#from .forms import ContactForm
#from django.contrib import messages
#from django.http import HttpResponseRedirect
#from django.core.mail import send_email


# Create your views here.
#def index(request):
 #   return render(request,'index.html')

#def conn(request):
 #   form = ContactForm(request.POST or None)
  #  if form.is_valid():
   #     form.save()
    #    form = ContactForm()
    #context = {'form':form}
    #send_mail(form,['chandravanshi.neha01@gmail.com'])
    #return render(request,'result.html', context)

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this
from django import forms
from .forms import ContactForm # Add this
from django.core.mail import send_mail


# Create your views here.
def index(request):
   return render(request,'index.html')

# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['chandravanshi.neha01@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})





