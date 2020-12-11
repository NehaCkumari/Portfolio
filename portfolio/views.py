from django.shortcuts import render,redirect
from .models import contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
#from django.core.mail import send_email


# Create your views here.
def index(request):
    return render(request,'index.html')

def conn(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {'form':form}
    send_mail(form,['chandravanshi.neha01@gmail.com'])
    return render(request,'result.html', context)







