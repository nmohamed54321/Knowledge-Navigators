from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactForm
from django.contrib import messages  

# This file renders all of the templates 

def home(request):
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html') 


def contact(request):
    #Checks if the form was submitted
    if request.method == 'POST':
        firstName = request.POST.get('firstName').strip()
        lastName = request.POST.get('lastName').strip()
        email = request.POST.get('email').strip()
        phoneNumber = request.POST.get('phoneNumber').strip()
        message = request.POST.get('message').strip()

        #Create the instance
        new_form = ContactForm(firstName=firstName, lastName=lastName, email=email, phoneNumber=phoneNumber, message=message)

        #Save the instance
        new_form.save()

        # Let's the user know the form has been submitted
        messages.success(request, 'Message sent successfully!')

        #Redirects the user to the same page
        return redirect('contact')

    #Render the contact page with the form
    return render(request, 'contact.html') 

        

def login(request):
    return render(request, 'login.html') #This renders login template
    

def signup(request):
    return render(request, 'signup.html') #This renders the signup template
    
