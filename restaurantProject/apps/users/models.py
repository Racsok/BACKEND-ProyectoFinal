from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Mesero
class Waiter(models.Model):
    CHARGE_CHOICES = [('MG', 'MANAGER'),('AT', 'ADMINTABLES'),('EX', 'EXTRA')]
    charge = models.CharField(max_length=2, choices=CHARGE_CHOICES, default='EX')
    
    def __str__(self) -> str:
        return f"{self.user.first_name}"
    
