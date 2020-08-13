from django.db import models

# Create your models here.


class geo(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

class Address(models.Model):
    street = models.CharField(max_length=30)
    suite = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    geo = models.ForeignKey(geo, on_delete=models.CASCADE,null=True, blank=True, default = None)

class Company(models.Model):
    name = models.CharField(max_length=30)
    catchPhrase = models.CharField(max_length=30)
    bs = models.CharField(max_length=30)
   
    def __str__(self):
        return self.name

    
class User (models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, default = None)
    phone = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete = models.PROTECT, null=True, blank=True, default = None)
    
    def __str__(self):
        return self.username

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.body