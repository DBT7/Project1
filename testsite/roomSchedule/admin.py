from django.contrib import admin

# Register your models here.


# from roomSchedule.models import Address,Building,Person,Organization
 
# class AddressAdmin(admin.ModelAdmin):
#     list_display=('address',)
 
 
  
# class BuildingAdmin(admin.ModelAdmin):
#     list_display=('name',)
 
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display=('orgname',)
 
# class PersonAdmin(admin.ModelAdmin):
#     list_display=('firstname','lastname','email')
 
# admin.site.register(Address,AddressAdmin)
# admin.site.register(Building,BuildingAdmin)
# admin.site.register(Organization,OrganizationAdmin)
# admin.site.register(Person,PersonAdmin)


#from roomSchedule.models import Address,Building,Person,Organization

from .models import Reservation,Room,Building


admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Building)



