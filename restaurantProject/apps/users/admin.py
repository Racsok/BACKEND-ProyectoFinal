from django.contrib import admin
from .models import *
# Register your models here.

class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user", "charge"]
    
class WaiterShiftAdmin(admin.ModelAdmin):
    list_display = ["waiter", "restaurant", "start_date", "end_date"]
    
class TipWaiterAdmin(admin.ModelAdmin):
    list_display = ["bill", "waiter", "paid"]
    
        
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(WaiterShift, WaiterShiftAdmin)
admin.site.register(TipWaiter, TipWaiterAdmin)