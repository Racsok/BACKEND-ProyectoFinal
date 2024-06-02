from django.contrib import admin
from .models import *
# Register your models here.

class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user", "charge"]
    
class WaiterShiftAdmin(admin.ModelAdmin):
    list_display = ["waiter", "restaurant", "start_date", "end_date"]
    
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(WaiterShift, WaiterShiftAdmin)