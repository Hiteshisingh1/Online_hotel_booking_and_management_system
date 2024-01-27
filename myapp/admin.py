from django.contrib import admin
from .models import Staff, ExtendedUser, Contact, Hotel, FinalBooking, CorImg

# Register your models here.

admin.site.register(Staff)
admin.site.register(ExtendedUser)
admin.site.register(Contact)
admin.site.register(FinalBooking)
admin.site.register(Hotel)
admin.site.register(CorImg)
