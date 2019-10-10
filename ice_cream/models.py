from django.db import models
from datetime import date
from django.urls import reverse

class IceCream(models.Model):

    CHOCOLATE = 'CHOCOLATE'
    VANILLA = 'VANILLA'

    WEEKLY = 'WEEKLY'
    DAILY = 'DAILY'
    SEASONAL = 'SEASONAL'

    AVAILABLE_CHOICES = [
        (WEEKLY, 'Weekly'),
        (DAILY, 'Daily'),
        (SEASONAL, 'Seasonal'),
    ]

    BASE_CHOICES = [
        (CHOCOLATE, 'Chocolate'),
        (VANILLA, 'Vanilla'),
    ]

    flavor = models.CharField(max_length=255)
    available = models.CharField(max_length=255, choices=AVAILABLE_CHOICES)
    base = models.CharField(max_length=255, choices=BASE_CHOICES)
    featured = models.BooleanField(default=False)
    churn_date = models.DateField('date churned', default=date.today)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse('ice_cream:index')
