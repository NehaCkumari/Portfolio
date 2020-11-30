from django.shortcuts import render,redirect
from .models import contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def conn(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {'form':form}
    return render(request,'result.html', context)







