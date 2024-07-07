from django.contrib import admin #This line imports the admin module
from .models import ContactForm #This line imports the ContactForm 


# Register your models here.
admin.site.register(ContactForm)

