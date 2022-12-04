from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('allCars/', views.getAllCars, name='allCars'),
    path('allLicenses/', views.getAllLicenses, name='allLicenses'),
    path('allOwners/', views.getAllOwners, name='allOwners'),
    path('allEngines/', views.getAllEngines, name='allEngines'),
    path('allGasStations/', views.getAllGasStations, name='allGasStations'),
    path('allGasStationCars/', views.getAllGasStationCar, name='allGasStationCars'),
    
    path('randomData/', views.generateData, name='randomData'),
    path('deleteData/', views.deleteData, name='deleteData'),

    path('addCar/', views.addCarData, name='addCar'),
    path('deleteCar/', views.deleteCarData, name='deleteCar'),
    path('updateCar/', views.updateCarData, name='updateCar'),
    path('generateCarData/', views.generateCarData, name='generateCars'),
    
    path('addGasStationCar/', views.addGasStationCarData, name='addGasStationCar'),
    path('updateGasStationCar/', views.updateGasStationCarData, name='updateGasStationCar'),
    path('deleteGasStationCar/', views.deleteGasStationCarData, name='deleteGasStationCar'),

    path('addOwner/', views.addOwnerData, name='addOwner'),
    path('updateOwner/', views.updateOwnerData, name='updateOwner'),
    path('deleteOwner/', views.deleteOwnerData, name='deleteOwner'),

    path('addLicense/', views.addLicenseData, name='addLicense'),
    path('updateLicense/', views.updateLicenseData, name='updateLicense'),
    path('deleteLicense/', views.deleteLicenseData, name='deleteLicense'),

    path('addGasStation/', views.addGasStationData, name='addGasStation'),
    path('updateGasStation/', views.updateGasStationData, name='updateGasStation'),
    path('deleteGasStation/', views.deleteGasStationData, name='deleteGasStation'),

    path('addEngine/', views.addEngineData, name='addEngine'),
    path('updateEngine/', views.updateEngineData, name='updateEngine'),
    path('deleteEngine/', views.deleteEngineData, name='deleteEngine'),
]