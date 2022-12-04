from django.db import models, connection
from abc import ABC, abstractmethod

class CustomModel(ABC):

    def __init__(self):
        self.name = "abc"

    @abstractmethod
    def addData(self, data): 
        pass

    def showData(self):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from {self.name}")
            data = cursor.fetchall()
            print(data)
            return data


    @abstractmethod
    def updateData(self):
        pass

    @abstractmethod
    def deleteData(self):
        pass

    @abstractmethod
    def generateData(self):
        pass


class Car(CustomModel):
    def __init__(self):
        self.name = 'Car'
    
    def addData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Car (car_vin, car_brand, car_type, car_registration) VALUES ('{data['car_vin']}', '{data['car_brand']}', '{data['car_type']}', '{data['car_registration']}')")
            
        

    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE CAR SET car_brand='{data['car_brand']}', car_type='{data['car_type']}', car_registration='{data['car_registration']}' where car_vin='{data['car_vin']}'")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise
        
    def deleteData(self, id):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Car where car_vin='{id}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass


class Owner(CustomModel):
    def __init__(self):
        self.name = 'Owner'
    
    def addData(self, data):
         with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Owner (owner_name, owner_license, owner_car_registration) VALUES ('{data['owner_name']}', '{data['owner_license']}', '{data['owner_car_registration']}')")

    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE Owner SET owner_name='{data['owner_name']}', owner_license='{data['owner_license']}' where owner_car_registration='{data['owner_car_registration']}'")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise

    def deleteData(self, id):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Owner where owner_car_registration='{id}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass

class GasStation(CustomModel):
    def __init__(self):
        self.name = 'Gas_Station'
    
    def addData(self, data):
        with connection.cursor() as cursor:
            try:
                data['gas_station']  = int(data['gas_station'])
            except:
                raise Exception("wrong gas station id")

            try:
                data['gas_station']  = int(data['gas_station'])
            except:
                raise Exception("wrong gas station number")
            cursor.execute(f"INSERT INTO Gas_Station(gas_station_id, gas_station_name, gas_station) VALUES({data['gas_station_id']}, '{data['gas_station_name']}', {data['gas_station']})")

    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE gas_station SET gas_station_name='{data['gas_station_name']}', gas_station_size={data['gas_station_size']} where gas_station_id={data['gas_station_id']}")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise

    def deleteData(self, id):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Gas_Station where gas_station_id='{id}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass

class Engine(CustomModel):
    def __init__(self):
        self.name = 'Engine'

    def addData(self, data):
        with connection.cursor() as cursor:
            try:
                data['engine_power'] = int(data['engine_power'])
            except:
                raise Exception("wrong engine power")
            
            try:
                data['engine_volume'] = float(data['engine_volume'])
            except:
                raise Exception("wrong engine volume")
            
            cursor.execute(f"INSERT INTO Engine (engine_code, engine_vin, engine_volume, engine_power, engine_type) VALUES ('{data['engine_code']}', '{data['engine_vin']}', {data['engine_volume']}, {data['engine_power']}, '{data['engine_type']}')")

    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE engine SET engine_volume={data['engine_volume']}, engine_type='{data['engine_type']}', engine_power={data['engine_power']} where engine_code='{data['engine_code']}' and engine_vin='{data['engine_vin']}'")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise

    def deleteData(self, enid, envin):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Engine where engine_code='{enid}' and engine_vin='{envin}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass


class OwnerLicense(CustomModel):
    def __init__(self):
        self.name = "Owner_license"

    def addData(self, data): 
        with connection.cursor() as cursor:
            try:
                data['owner_experience'] = int(data['owner_experience'])
            except:
                raise Exception("wrong experience")

            cursor.execute(f"INSERT INTO {self.name}(owner_license, owner_experience) VALUES('{data['owner_license']}',{data['owner_experience']})")

    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE Owner_license SET owner_experience='{data['owner_experience']}' where owner_license='{data['owner_license']}'")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise

    def deleteData(self, id):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {self.name} where owner_license='{id}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass

class GasStationCar(CustomModel):
    def __init__(self):
        self.name = "gas_station_car"

    def addData(self, data): 
        with connection.cursor() as cursor:
            try:
                data['amount_of_fuel'] = int(data['amount_of_fuel'])
            except:
                raise Exception("wrong amount of fuel")

            cursor.execute(f"INSERT INTO {self.name}(gas_station_id, car_vin, by_whom, fuel_type, amount_of_fuel) VALUES({data['gas_station_id']},'{data['car_vin']}', '{data['by_whom']}', '{data['fuel_type']}', {data['amount_of_fuel']})")

        
    def updateData(self, data):
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE gas_station_car SET by_whom='{data['by_whom']}', fuel_type='{data['fuel_type']}', amount_of_fuel='{data['amount_of_fuel']}' where gas_station_id='{data['gas_station_id']}' and car_vin='{data['car_vin']}'")
            affected_rows = cursor.rowcount
            if affected_rows == 0:
                raise

    def deleteData(self, gsid, cvin):
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {self.name} where gas_station_id='{gsid}' and car_vin='{cvin}'")
            deleted_rows = cursor.rowcount
            if deleted_rows == 0:
                raise

    def generateData(self):
        pass