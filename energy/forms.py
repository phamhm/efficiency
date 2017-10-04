from django.forms import ModelForm
from .models import EnergyCapture


class EnergyCaptureForm(ModelForm):
    class Meta:
        model = EnergyCapture
        fields = ['energy_level']
