from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=50)

class customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    pwd=models.CharField(max_length=50)
    phno=models.CharField(max_length=10)
    #address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    psd=models.CharField(max_length=10)
    class Meta:
        db_table="customer"
    def __str__(self):
        return self.email+"  "+self.name+"  "+self.phno+"  "+self.pwd+"  "+self.city+"  "+self.pin+"  "+self.psd+"  "

class admins(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pswd=models.CharField(max_length=50)
    class Meta:
        db_table="admins"
    def __str__(self):
        return self.name+"  "+self.phno+"  "+self.email+"  "+self.pswd+"  "

class reserve(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    date=models.CharField(max_length=255)
    seats=models.CharField(max_length=50)
    class Meta:
        db_table="reserve"
    def __str__(self):
        return self.name+"  "+self.phno+"  "+self.date+"  "+self.seats+"  "
        
class contactt(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    comment=models.CharField(max_length=255)
    class Meta:
        db_table="contactt"
    def __str__(self):
        return self.name+"  "+self.email+"  "+self.comment+"  "