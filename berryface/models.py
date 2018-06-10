from django.db import models

# Create your models here.
class MeasureType(models.Model):
    measurement = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

class SensorType(models.Model):
    name = models.CharField(max_length=100)
    measurements = models.ManyToManyField(Measuretype)

class Sensor(models.Model):
    given_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)

class Entry(models.Model):
    given_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)

class Entry(models.Model):
    value = models.FloatField()
    date = models.DateTimeField()
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    measure_type_id = models.ForeignKey(MeasureType, on_delete=models.CASCADE)
