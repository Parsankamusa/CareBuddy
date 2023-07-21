
# Create your models here.
from django.db import models


class Donations(models.Model):
    """Model for  donations."""

    donor_name = models.CharField(max_length=255)
    donor_address = models.CharField(max_length=255)
    donor_Email = models.EmailField(blank = True, null=True)
    donor_mobile = models.CharField(max_length=20)
    Donation_type = models.CharField(max_length=255)

    request = models.TextField(blank = True, null=True)
    
    accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    
    
    category = models.ManyToManyField('Category', related_name='item')


    def __str__(self):
        return self.donor_name

    class Meta:
        ordering = ["-created_at"] 



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
