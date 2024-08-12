from django.contrib import admin
from .models import Appointment
# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient','specialty','appointment_date', 'appointment_time')
    search_fields = ('doctor__name', 'patient__name')
    list_filter = ('doctor', 'appointment_date')