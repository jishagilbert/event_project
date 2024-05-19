from django.contrib import admin

from evenapp.models import photo, Booking, Review,Contact

# Register your models here.
admin.site.register(photo)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Contact)