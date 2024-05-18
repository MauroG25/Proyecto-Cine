from django.contrib import admin

from .models import  User,CinemaHall,Movie,Ticket

# Register your models here.
admin.site.register(CinemaHall)
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(User)
# Register your models here.
