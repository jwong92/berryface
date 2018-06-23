from django.contrib import admin

# Register your models here.
from .models import MeasureType, SensorType, Sensor, Entry, Role, User
admin.site.register(MeasureType)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Entry)
admin.site.register(User)
admin.site.register(Role)

