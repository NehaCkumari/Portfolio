from django.shortcuts import render,redirect
from .models import contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_email


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
    return render(request,'result.html', context)'''

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['chandravanshi.neha01@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "index.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')'''







