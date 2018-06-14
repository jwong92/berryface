from django.db import models

# Create your models here.
class MeasureType(models.Model):
    measurement = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.measurement

class SensorTypeManager(models.Manager):
    def insert_sensor(self, sensors):
        # FOR EACH SENSOR FROM JSON
        for sensor in sensors:
            # IF THE SENSOR DOESN'T EXIST
            s = self.filter(name=sensor['sensor_type_name']).exists()
            if not s:
                measuretypes = []
                # FOR EACH TYPE OF SENSOR
                for mtype in sensor['types']:
                    m = MeasureType.objects.filter(measurement=mtype['measure'])
                    # IF THE MEASUREMENT TYPE DOESN'T EXIST
                    if not m:
                        # ADD THE MEASUREMENT TYPE, APPEND THE ID OF THIS TO THE ARRAY
                        m = MeasureType(measurement=mtype['measure'], unit=mtype['unit'])
                        m.save()
                        m = MeasureType.objects.filter(measurement=mtype['measure'])
                    measuretypes.append(m.values()[0]['id'])
                # ADD A NEW SENSOR
                new_sensor_type = SensorType(name=sensor['sensor_type_name'])
                new_sensor_type.save()
                # ADD THE ID OF THE MEASUREMENT TO MAKE THE RELATIONSHIP TO THE SENSOR
                for m_id in measuretypes:
                    new_sensor_type.measurements.add(m_id)
        return "Sensor Added"

class SensorType(models.Model):
    name = models.CharField(max_length=100)
    measurements = models.ManyToManyField(MeasureType)
    objects = SensorTypeManager()

    def __str__(self):
        return self.name

    def get_json_entries(self, sensor):
        types_json = []
        types = self.measurements.all()
        for item in types:
            entries = []
            entries_objects = Entry.objects.filter(sensor_type_id_id=sensor.id).filter(sensor_type_id_id = item.id)
            for entry in entries_objects:
                entries.append(entry.get_json())
            types_json.append({"measure": item.measurement,
                            "unit": item.unit,
                            "entries": entries})
        return types_json

class SensorManager(models.Manager):
    def get_all_json(self, filter_date):
        sensors_all = self.all()

        json_all = []
        for item in sensors_all:
            json_all.append(item.get_json_with_relations(filter_date))
        return json_all


class Sensor(models.Model):
    objects = SensorManager()
    given_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)

    def get_json_with_relations(self, filter_date):
        return {
            "sensor_type_name": self.sensor_type_id.name,
            "given_name": self.given_name,
            "location": self.location,
            "types": self.sensor_type_id.get_json_entries(self)
        }


class Entry(models.Model):
    given_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)

class Entry(models.Model):
    value = models.FloatField()
    date = models.DateTimeField()
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    measure_type_id = models.ForeignKey(MeasureType, on_delete=models.CASCADE)