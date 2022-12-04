from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import *

def index(request):
    return render(request, 'carDiagnosis/index.html', {})


def getAllCars(request):
    cars = Car()
    car = cars.showData()
    return render(request, 'carDiagnosis/allCars.html', {
        'carList' : car,
    })

def addCarData(request):
    if(request.method == 'POST'):
        cars = Car()

        cars.addData({
            'car_vin': request.POST.get('car_vin', ''),
            'car_brand': request.POST.get('car_brand', ''),
            'car_type': request.POST.get('car_type', ''),
            'car_registration': request.POST.get('car_registration', ''),
        })

        return redirect('index')


    with connection.cursor() as cursor:
        cursor.execute("SELECT owner_car_registration from Owner")

        options = cursor.fetchall()

        optionsList = []

        for option in options:
            optionsList.append(option[0])

    return render(request, 'carDiagnosis/addCar.html', {
        'carRegistrationOptions': optionsList,
    })

def deleteCarData(request):
    cars = Car()
    cars.deleteData(request.GET['id'])

    return redirect('allCars')

def updateCarData(request):
    if(request.method == 'POST'):
        cars = Car()
        cars.updateData({
            'car_vin': request.GET.get('id', ''),
            'car_brand': request.POST.get('car_brand', ''),
            'car_type': request.POST.get('car_type', ''),
            'car_registration': request.POST.get('car_registration', ''),
        })

        redirect('allCars')
    
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from Car WHERE car_vin='{request.GET.get('id')}'")
        car = cursor.fetchall()
        
        cursor.execute("SELECT owner_car_registration from Owner")
        options = cursor.fetchall()
        optionsList = []

        for option in options:
            optionsList.append(option[0])

    return render(request, 'carDiagnosis/updateCar.html', {
        'car': car[0],
        'carRegistrationOptions': optionsList,
    })


def updateGasStationData(request):
    if(request.method == "POST"):
        gasStation = GasStation()

        gasStation.updateData({
            'gas_station_id': request.GET.get('id', ''),
            'gas_station_name': request.POST.get('gas_station_name', ''),
            'gas_station_size': request.POST.get('gas_station_size', ''),
        })

        redirect('allGasStations')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from gas_station WHERE gas_station_id='{request.GET.get('id')}'")
        gasStation = cursor.fetchall()


    return render(request, 'carDiagnosis/updateGasStation.html', {
        'gasStation': gasStation[0],
    })





def addOwnerData(request):
    if(request.method == 'POST'):
        owners = Owner()

        owners.addData({
            'owner_name': request.POST.get('owner_name', ''),
            'owner_license': request.POST.get('owner_license', ''),
            'owner_car_registration': request.POST.get('owner_car_registration', ''),
        })

    with connection.cursor() as cursor:
        cursor.execute("SELECT owner_license from Owner_license WHERE NOT EXISTS(SELECT 1 FROM Owner WHERE Owner.owner_license = owner_license.owner_license)")

        options = cursor.fetchall()

        optionsList = []

        for option in options:
            optionsList.append(option[0])

    return render(request, 'carDiagnosis/addOwner.html', {
        'licenseOptions': optionsList,
    })

def updateOwnerData(request):
    if(request.method == "POST"):
        owner = Owner()

        owner.updateData({
            'owner_car_registration': request.GET.get('id', ''),
            'owner_name': request.POST.get('owner_name', ''),
            'owner_license': request.POST.get('owner_license', ''),
        })

        redirect('allOwners')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from Owner WHERE owner_car_registration='{request.GET.get('id')}'")
        owner = cursor.fetchall()
        
        cursor.execute(f"SELECT owner_license FROM owner WHERE owner_car_registration='{request.GET.get('id')}'")

        options = cursor.fetchall()

        optionsList = []

        for option in options:
            optionsList.append(option[0])

    return render(request, 'carDiagnosis/updateOwner.html', {
        'owner': owner[0],
        'licenseOptions': optionsList,
    })

def updateEngineData(request):
    if(request.method == "POST"):
        engine = Engine()

        engine.updateData({
            'engine_code': request.GET['id'].split()[0],
            'engine_vin': request.GET['id'].split()[1],
            'engine_volume': request.POST.get('engine_volume', ''),
            'engine_type': request.POST.get('engine_type', ''),
            'engine_power': request.POST.get('engine_power', ''),
        })

        redirect('allEngines')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from engine WHERE engine_code='{request.GET['id'].split()[0]}' and engine_vin='{request.GET['id'].split()[1]}'")
        engine = cursor.fetchall()


    return render(request, 'carDiagnosis/updateEngine.html', {
        'engine': engine[0],
    })



def updateLicenseData(request):
    if(request.method == "POST"):
        license = OwnerLicense()

        license.updateData({
            'owner_license': request.GET.get('id', ''),
            'owner_experience': request.POST.get('owner_experience', ''),
        })

        redirect('allLicenses')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from owner_license WHERE owner_license='{request.GET.get('id')}'")
        license = cursor.fetchall()


    return render(request, 'carDiagnosis/updateLicense.html', {
        'license': license[0],
    })

def deleteOwnerData(request):
    owners = Owner()
    owners.deleteData(request.GET['id'])

    return redirect('allOwners')

def addGasStationData(request):
    if(request.method == 'POST'):
        gasStations = GasStation()

        gasStations.addData({
            'gas_station_id': request.POST.get('gas_station_id', ''),
            'gas_station_name': request.POST.get('gas_station_name'),
            'gas_station': request.POST.get('gas_station'),
        })

    return render(request, 'carDiagnosis/addGasStation.html')

def deleteGasStationData(request):
    gasStations = GasStation()
    gasStations.deleteData(request.GET['id'])
    
    return redirect('allGasStations')



def addEngineData(request):
    if(request.method == 'POST'):
        engines = Engine()

        engines.addData({
            'engine_code': request.POST.get('engine_code', ''),
            'engine_vin': request.POST.get('engine_vin', ''),
            'engine_volume': request.POST.get('engine_volume', ''),
            'engine_type': request.POST.get('engine_type', ''),
            'engine_power': request.POST.get('engine_power', ''),
        })

    with connection.cursor() as cursor:
        cursor.execute("SELECT car_vin from Car")

        options = cursor.fetchall()

        optionsList = []

        for option in options:
            optionsList.append(option[0])

    return render(request, 'carDiagnosis/addEngine.html', {
        'carVinOptions': optionsList,
    })

def addGasStationCarData(request):
    if(request.method == 'POST'):
        gasStationCars = GasStationCar()

        gasStationCars.addData({
            'gas_station_id': request.POST.get('gas_station_id', ''),
            'car_vin': request.POST.get('car_vin', ''),
            'by_whom': request.POST.get('by_whom', ''),
            'fuel_type': request.POST.get('fuel_type', ''),
            'amount_of_fuel': request.POST.get('amount_of_fuel', ''),
        })

    with connection.cursor() as cursor:
        cursor.execute("SELECT car_vin from Car")
        options = cursor.fetchall()
        carVinoptionsList = []
        
        for option in options:
            carVinoptionsList.append(option[0])

        cursor.execute("SELECT gas_station_id from Gas_station")
        options = cursor.fetchall()
        gasStationIdList = []

        for option in options:
            gasStationIdList.append(option[0])

    return render(request, 'carDiagnosis/addGasStationCar.html', {
        'carVinOptions': carVinoptionsList,
        'gasStationIdOptions': gasStationIdList,
    })

def updateGasStationCarData(request):
    if(request.method == 'POST'):
        gasStationCar = GasStationCar()

        gasStationCar.updateData({
            'gas_station_id': request.GET['id'].split()[0],
            'car_vin': request.GET['id'].split()[1],
            'by_whom': request.POST.get('by_whom', ''),
            'fuel_type': request.POST.get('fuel_type', ''),
            'amount_of_fuel': request.POST.get('amount_of_fuel', ''),
        })

        redirect('allGasStationCars')

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * from Gas_Station_car WHERE car_vin='{request.GET['id'].split()[1]}' and gas_station_id='{request.GET['id'].split()[0]}'")
        gasStationCar = cursor.fetchall()

        print(gasStationCar)
    return render(request, 'carDiagnosis/updateGasStationCar.html', {
        'gasStationCar': gasStationCar[0],
    })

def addLicenseData(request):
    if(request.method == 'POST'):
        licenses = OwnerLicense()

        licenses.addData({
            'owner_license': request.POST.get('owner_license', ''),
            'owner_experience': request.POST.get('owner_experience', ''),
        })

    return render(request, 'carDiagnosis/addLicense.html', {})

def deleteEngineData(request):
    engines = Engine()
    engines.deleteData(request.GET['id'].split()[0], request.GET['id'].split()[1])

    return redirect('allEngines')

def deleteLicenseData(request):
    licenses = OwnerLicense()
    licenses.deleteData(request.GET['id'])

    return redirect('allLicenses')

def deleteGasStationCarData(request):
    gasStationCars = GasStationCar()

    gasStationCars.deleteData(request.GET['id'].split()[0], request.GET['id'].split()[1])
    
    return redirect('allGasStationCars')




def generateCarData(request):
    pass

def getAllLicenses(request):
    licenses = OwnerLicense()
    license = licenses.showData()
    return render(request, 'carDiagnosis/allLicenses.html', {
        'licenseList' : license,
    })

def getAllGasStationCar(request):
    gasStationCars = GasStationCar()
    gasStationCar = gasStationCars.showData()
    return render(request, 'carDiagnosis/allGasStationCar.html', {
        'gasStationCarList': gasStationCar,
    })


def getAllOwners(request):
    owners = Owner()
    owner = owners.showData()
    return render(request, 'carDiagnosis/allOwners.html', {
        'ownerList' : owner,
    })

def getAllGasStations(request):
    gasStations = GasStation()
    gasStation = gasStations.showData()

    return render(request, 'carDiagnosis/allGasStation.html', {
        'gasStationList': gasStation,
    })

def getAllEngines(request):
    engines = Engine()
    engine = engines.showData()

    return render(request, 'carDiagnosis/allEngines.html', {
        'engineList': engine,
    })

def deleteData(request):
    with connection.cursor() as cursor:
        cursor.execute('''truncate owner_license cascade;
        truncate gas_station cascade
        ''')

    return redirect('index')

def generateData(request):
    with connection.cursor() as cursor:
            cursor.execute(f'''Create or replace function random_string(length integer) returns text as
            $$
            declare
            result text := '';
            i integer := 0;
            begin
            if length < 0 then
                raise exception 'Given length cannot be less than 0';
            end if;
            for i in 1..length loop
                result := result || chr(trunc(97+random()*25)::int);
            end loop;
            return result;
            end;
            $$ language plpgsql;''')

            cursor.execute(f'''do $$
            begin
            for cnt in 1..5 loop
                insert into owner_license(owner_license, owner_experience) values(random_string(5), trunc(random()*100)::int);
                insert into owner(owner_car_registration, owner_name, owner_license) values(random_string(10), random_string(5), (select owner_license from(SELECT owner_license from Owner_license WHERE NOT EXISTS(SELECT 1 FROM Owner WHERE Owner.owner_license = owner_license.owner_license)) as foo ORDER BY random() limit 1));
                insert into gas_station(gas_station_id, gas_station_name, gas_station_size) values(trunc(random()*10000)::int, random_string(10), trunc(random()*10)::int);
                insert into car(car_vin, car_brand, car_type, car_registration) values(random_string(10), random_string(10), random_string(10), (select owner_car_registration from(select owner_car_registration from owner where not exists(select 1 from car where car_registration = owner_car_registration)) as foo order by random() limit 1 ));
                insert into gas_station_car(gas_station_id, car_vin, by_whom, fuel_type, amount_of_fuel) values((select gas_station_id from (select gas_station_id from gas_station where not exists(select 1 from gas_station_car where gas_station_car.gas_station_id = gas_station.gas_station_id)) as boo ORDER BY random() limit 1), (select car_vin from (select car_vin from car where not exists(select 1 from gas_station_car where gas_station_car.car_vin = car.car_vin)) as foo ORDER BY random() limit 1), random_string(5), trunc(random()*100)::int, trunc(random()*100)::int);
                insert into engine(engine_code, engine_vin, engine_volume, engine_type, engine_power) values(random_string(15), (select car_vin from (select car_vin from car where not exists(select 1 from engine where engine.engine_vin = car.car_vin)) as foo ORDER BY random() limit 1), trunc(random()*10)/random()/3::float, random_string(10), trunc(random()*100)::int);
            end loop;  
            end; $$ ''')

    return redirect('index')


def show(request):
    if(request.method == 'POST'):
        if(request.POST.get('table_type', '') == 'engine'):
            with connection.cursor() as cursor:
                if(request.POST.get('filter', '') != ''):
                    cursor.execute(f"select * from engine inner join car on car.car_vin=engine.engine_vin where car_brand='{request.POST.get('filter', '')}'")
                else:
                    cursor.execute(f"select * from engine inner join car on car.car_vin=engine.engine_vin")
                listOptions = cursor.fetchall()

                return render(request, 'carDiagnosis/showData.html', {
                    'listOptions': listOptions,
                })
        elif(request.POST.get('table_type', '') == 'car'):
            with connection.cursor() as cursor:
                if(request.POST.get('filter', '') == ''):

                    cursor.execute(f"select * from car inner join owner on owner.owner_car_registration=car.car_registration")
                else:
                    cursor.execute(f"select * from car inner join owner on owner.owner_car_registration=car.car_registration where owner_name='{request.POST.get('filter', '')}'")
                listOptions = cursor.fetchall()

                return render(request, 'carDiagnosis/showData.html', {
                    'listOptions': listOptions,
                })
        else:
            with connection.cursor() as cursor:
                if(request.POST.get('filter', '') == ''):
                    cursor.execute(f"select * from owner_license inner join owner on owner.owner_license=owner_license.owner_license")
                else:
                    cursor.execute(f"select * from owner_license inner join owner on owner.owner_license=owner_license.owner_license where owner_experience >= {request.POST.get('filter','')}")
                listOptions = cursor.fetchall()

                return render(request, 'carDiagnosis/showData.html', {
                        'listOptions': listOptions,
                    })

    with connection.cursor() as cursor:
        cursor.execute(f"select * from car inner join owner on owner.owner_car_registration=car.car_registration")
        listOptions = cursor.fetchall()

        return render(request, 'carDiagnosis/showData.html', {
            'listOptions': listOptions,
        })


    