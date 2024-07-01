from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm

# This file renders all of the templates 

def home(request):
    return HttpResponse('Hello, World!') 
    #return render(request, 'home.html') #This renders the home.html template
    # If this doesn't work, try: 'learnovation_launchpad/home.html'

def about(request):
    return render(request, 'about.html') #This renders the about.html template
    # If this doesn't work, try: 'learnovation_launchpad/about.html'

def contact(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        message = request.POST['message']

        #Save the form data to the database
        contact_form = ContactForm(firstName=firstName, lastName=lastName, email=email, phoneNumber=phoneNumber, message=message)
        contact_form.save()

        return HttpResponse('Thank you for your submission!')
        
    return render(request, 'contact.html') #This renders the contact.html template
    

