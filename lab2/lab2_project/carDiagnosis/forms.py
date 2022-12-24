from django.forms import ModelForm
from .models import *

class LicenseForm(ModelForm):
    class Meta:
        model = OwnerLicense
        fields = '__all__'

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class EngineForm(ModelForm):
    class Meta:
        model = Engine
        fields = '__all__'

class GasStationForm(ModelForm):
    class Meta:
        model = GasStation
        fields = '__all__'

class GasStationCarForm(ModelForm):
    class Meta:
        model = GasStationCar
        fields = '__all__'