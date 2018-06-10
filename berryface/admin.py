from django.contrib import admin

# Register your models here.
from .models import MeasureType, SensorType, Sensor, Entry
admin.site.register(MeasureType)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Entry)

