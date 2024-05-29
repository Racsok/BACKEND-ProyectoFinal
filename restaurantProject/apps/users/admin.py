from django.contrib import admin
from .models import *
# Register your models here.

class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user", "charge"]
    
admin.site.register(Waiter, WaiterAdmin)