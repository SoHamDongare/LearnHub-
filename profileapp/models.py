from django.db import models

# Create your models here.
class Profile(models.Model):
    genderChoice=[
       ("male","male"),
       ("female","female"),
       ("other","other")          
    ]
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    contact=models.CharField(max_length=20)
    gender=models.CharField(choices=genderChoice,max_length=20)
    image=models.FileField(upload_to="uploads/")
    def __str__(self):
        return self.fullname
