from django.db import models

class OwnerLicense(models.Model):
    owner_license = models.CharField(primary_key=True, max_length=20)
    owner_experience = models.IntegerField()
    def __str__(self):
        return self.owner_license

class Owner(models.Model):
    owner_car_registration = models.CharField(primary_key=True, max_length=20)
    owner_name = models.CharField(max_length=30)
    owner_license = models.ForeignKey(OwnerLicense, on_delete=models.CASCADE, to_field='owner_license')
    def __str__(self):
        return self.owner_car_registration

class Car(models.Model):
    car_vin = models.CharField(primary_key=True, max_length=10)
    car_brand = models.CharField(max_length=10)
    car_type = models.CharField(max_length=10)
    car_registration = models.ForeignKey(Owner, to_field='owner_car_registration', on_delete=models.CASCADE)
    def __str__(self):
        return self.car_vin

class Engine(models.Model):
    class Meta:
        unique_together = (('engine_vin', 'engine_code'),)
    engine_vin = models.ForeignKey(Car, on_delete=models.CASCADE, primary_key=True, to_field='car_vin')
    engine_code = models.CharField(max_length=10)
    engine_volume = models.FloatField()
    engine_type = models.CharField(max_length=10)
    engine_power = models.IntegerField()
    def __str__(self):
        return self.engine_code

class GasStation(models.Model):
    gas_station_id = models.AutoField(primary_key=True)
    gas_station_name = models.CharField(max_length=15)
    gas_station_size = models.IntegerField()
    def __str__(self):
        return str(self.gas_station_id)

class GasStationCar(models.Model):
    class Meta:
        unique_together = (('gas_station_id', 'car_vin'), )

    gas_station_id = models.ForeignKey(GasStation, on_delete=models.CASCADE, primary_key=True, to_field='gas_station_id')
    car_vin = models.ForeignKey(Car, on_delete=models.CASCADE, to_field='car_vin')
    by_whom = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=8)
    amount_of_fuel = models.IntegerField()
    def __str__(self):
        return self.gas_station_id

