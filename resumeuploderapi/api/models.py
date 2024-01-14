from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state_choices=(('Bihar','Bihar'),
                   ('Jharkhand','Jharkhand'),
                   ('West Bengal','West Bengal'),
                   
                   )
    state=models.CharField(max_length=50,choices=state_choices)
    gender=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='pimages',blank=True)
    rdoc=models.FileField(upload_to='rdoc',blank=True)

