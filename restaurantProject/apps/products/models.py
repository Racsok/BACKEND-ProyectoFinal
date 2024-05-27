from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=60, null = False, blank = False)
    cost_per_unit = models.IntegerField(default = 0, null = False, blank = False)
    all_restaurants = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name