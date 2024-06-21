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
