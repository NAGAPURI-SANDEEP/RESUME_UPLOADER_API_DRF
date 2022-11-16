from django.db import models

# Create your models here.

STATE_CHOICE=((
    ('CHENNAI','CHENNAI'),
    ('HYDERABAD','HYDERABAD'),
    ('BENGULURU','BENGULURU'),
    ('MUMBAI','MUMBAI'),
    ('NOIDA','NOIDA'),
))

class Profile(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Dob=models.DateField(auto_now=False,auto_now_add=False)
    State=models.CharField(choices=STATE_CHOICE,max_length=100)
    Gender=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Profile_pic=models.ImageField(upload_to='pimages',blank=True)
    File_upload=models.FileField(upload_to='files',blank=True)