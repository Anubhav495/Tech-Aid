from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class customuser(models.Model):
    username = models.CharField( max_length=100 )
    email = models.EmailField( )
    pass1 = models.CharField( max_length=20 )
    pass2 = models.CharField( max_length=20 )
    def __str__(self):
        return self.username