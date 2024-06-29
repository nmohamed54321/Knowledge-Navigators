from django.shortcuts import render
from django.http import HttpResponse

# This file renders all of the templates 

def home(request):
    return HttpResponse('Hello, World!') 
    #return render(request, 'home.html') #This renders the home.html template
    # If this doesn't work, try: 'learnovation_launchpad/home.html'

def about(request):
    return render(request, 'about.html') #This renders the about.html template
    # If this doesn't work, try: 'learnovation_launchpad/about.html'

def contact(request):
    return render(request, 'contact.html') #This renders the contact.html template
    # If this doesn't work, try: 'learnovation_launchpad/contact.html'

def login(request):
    return render(request, 'login.html') #This renders the login.html template
    # If this doesn't work, try: 'learnovation_launchpad/login.html'

def signup(request):
    return render(request, 'signup.html') #This renders the login.html template
    # If this doesn't work, try: 'learnovation_launchpad/login.html'