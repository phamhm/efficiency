from django.db import models

# Create your models here.


class EnergyCapture(models.Model):
    ENERGY_LEVELS = tuple((i, )*2 for i in range(0, 11))
    capture_time = models.DateTimeField(auto_now_add=True)
    energy_level = models.IntegerField(choices=ENERGY_LEVELS, default=10)

    def __str__(self):
        return '{} {}'.format(self.capture_time, self.energy_level)
