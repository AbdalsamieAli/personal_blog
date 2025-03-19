from django.shortcuts import render

from .models import Contact, Profile

profiles = Profile.objects.all()

def index(request):
    return render(request, 'profile_app/home.html', {'profiles': profiles})

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'profile_app/contact.html', {'contacts':contacts, 'profiles':profiles})


