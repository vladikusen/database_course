from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import *
from .forms import *

def index(request):
    return render(request, 'carDiagnosis/index.html', {})

def getAllLicenses(request):
    license_list = list(OwnerLicense.objects.all().values_list('owner_license', 'owner_experience'))
    return render(request, "carDiagnosis/allLicenses.html", {
        'all_licences': license_list,
    })

def getAllEngines(request):
    engines_list = list(Engine.objects.all().values_list('engine_vin', 'engine_code', 'engine_volume', 'engine_type', 'engine_power'))
    return render(request, "carDiagnosis/allEngines.html", {
        'all_engines': engines_list,
    })

def getAllOwners(request):
    owner_list = list(Owner.objects.all().values_list('owner_car_registration', 'owner_name', 'owner_license'))
    return render(request, "carDiagnosis/allOwners.html", {
        'all_owners': owner_list,
    })

def getAllCars(request):
    return render(request, "carDiagnosis/allCars.html", {
        'all_cars': list(Car.objects.all().values_list('car_vin', 'car_brand', 'car_type', 'car_registration')),
    })

def getAllGasStations(request):
    return render(request, "carDiagnosis/allGasStations.html", {
        'all_gas_stations': list(GasStation.objects.all().values_list('gas_station_id', 'gas_station_name', 'gas_station_size')),
    })

def getAllGasStationCars(request):
    return render(request, "carDiagnosis/allGasStationCars.html", {
        'all_gas_station_car': list(GasStationCar.objects.all().values_list('gas_station_id', 'car_vin', 'by_whom', 'fuel_type', 'amount_of_fuel'))
    })

def addOwner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allOwners')

    else:
        form = OwnerForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })



def addLicense(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allLicenses')

    else:
        form = LicenseForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def addCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allCars')

    else:
        form = CarForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def addEngine(request):
    if request.method == 'POST':
        form = EngineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allEngines')

    else:
        form = EngineForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def addGasStation(request):
    if request.method == 'POST':
        form = GasStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGasStations')

    else:
        form = GasStationForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def addGasStationCar(request):
    if request.method == 'POST':
        form = GasStationCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allGasStationCars')

    else:
        form = GasStationCarForm()

    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })


def editLicense(request, id):
    license = OwnerLicense.objects.filter(owner_license=id).first()
    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            return redirect('allLicenses')
    else:
        form = LicenseForm(instance=license)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })



def editOwner(request, id):
    owner = Owner.objects.filter(owner_car_registration=id).first()
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('allOwners')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def editCar(request, id):
    car = Car.objects.filter(car_vin=id).first()
    print(car)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('allCars')
    else:
        form = CarForm(instance=car)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def editEngine(request, id, id2):
    engine = Engine.objects.filter(engine_vin=id, engine_code=id2).first()
    if request.method == 'POST':
        form = EngineForm(request.POST, instance=engine)
        if form.is_valid():
            form.save()
            return redirect('allEngines')
    else:
        form = EngineForm(instance=engine)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def editGasStation(request, id):
    gas_station = GasStation.objects.filter(gas_station_id=id).first()
    if request.method == 'POST':
        form = GasStationForm(request.POST, instance=gas_station)
        if form.is_valid():
            form.save()
            return redirect('allGasStations')
    else:
        form = GasStationForm(instance=gas_station)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def editGasStationCar(request, id, id2):
    gas_station_car = GasStationCar.objects.filter(gas_station_id=id, car_vin=id2).first()
    if request.method == 'POST':
        form = GasStationCarForm(request.POST, instance=gas_station_car)
        if form.is_valid():
            form.save()
            return redirect('allGasStationCars')
    else:
        form = GasStationCarForm(instance=gas_station_car)
    return render(request, 'carDiagnosis/allEdit.html', {
        'form': form,
    })

def deleteLicense(request, id):
    OwnerLicense.objects.filter(owner_license=id).delete()
    return redirect('allLicenses')

def deleteOwner(request, id):
    Owner.objects.filter(owner_car_registration=id).delete()
    return redirect('allOwners')

def deleteCar(request, id):
    Car.objects.filter(car_vin=id).delete()
    return redirect('allCars')

def deleteEngine(request, id, id2):
    Engine.objects.filter(engine_vin=id, engine_code=id2).delete()
    return redirect('allEngines')

def deleteGasStation(request, id):
    GasStation.objects.filter(gas_station_id=id).delete()
    return redirect('allGasStations')

def deleteGasStationCar(requst, id, id2):
    GasStationCar.objects.filter(gas_station_id=id, car_vin=id2).delete()
    return redirect('allGasStationCars')
        