
# Create your models here.
from django.db import models






class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Donors(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()   
    donor_email = models.EmailField()
    Donation_type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    message = models.TextField(max_length= 1000, default='DEFAULT VALUE')
    
    def __str__(self):
       
        return f"{self.fullname} {self.donor_email} {self.mobile_number} Has donated {self.Donation_type} quantity {self.quantity} {self.message}"