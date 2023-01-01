from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allLicenses/', views.getAllLicenses, name='allLicenses'),
    path('allOwners/', views.getAllOwners, name='allOwners'),
    path('allCars/', views.getAllCars, name='allCars'),
    path('allEngines/', views.getAllEngines, name='allEngines'),
    path('allGasStations/', views.getAllGasStations, name='allGasStations'),
    path('allGasStationCars/', views.getAllGasStationCars, name='allGasStationCars'),
    path('addLicense/', views.addLicense, name='addLicense'),
    path('addOwner/', views.addOwner, name='addOwner'),
    path('addCar/', views.addCar, name='addCar'),
    path('addEngine/', views.addEngine, name='addEngine'),
    path('addGasStation/', views.addGasStation, name='addGasStation'),
    path('addGasStationCar/', views.addGasStationCar, name='addGasStationCar'),
    path('editCar/<str:id>/', views.editCar, name='editCar'),
    path('editLicense/<str:id>/', views.editLicense, name='editLicense'),
    path('editOwner/<str:id>/', views.editOwner, name='editOwner'),
    path('editEngine/<str:id>/<str:id2>/', views.editEngine, name='editEngine'),
    path('editGasStation/<str:id>/', views.editGasStation, name='editGasStation'),
    path('editGasStationCar/<str:id>/<str:id2>/', views.editGasStationCar, name='editGasStationCar'),
    path('deleteLicense/<str:id>/', views.deleteLicense, name='deleteLicense'),
    path('deleteOwner/<str:id>/', views.deleteOwner, name='deleteOwner'),
    path('deleteCar/<str:id>', views.deleteCar, name='deleteCar'),
    path('deleteEngine/<str:id>/<str:id2>/', views.deleteEngine, name='deleteEngine'),
    path('deleteGasStation/<str:id>/', views.deleteGasStation, name='deleteGasStation'),
    path('deleteGasStationCar/<str:id>/<str:id2>/', views.deleteGasStationCar, name='deleteGasStationCar'),
]