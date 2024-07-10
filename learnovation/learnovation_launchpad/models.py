from django.db import models


#Model created to save submitted contact form data
class ContactForm(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"



