from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Room(models.Model):

    # Setting choices to be used as currency for the price
    DOLARS = 'USD'
    MEXICAN_PESOS = 'MXN'
    COLOMBIAN_PESOS = 'COP'
    CURRENCY_CHOICES = [
        (DOLARS, 'Dolars'),
        (MEXICAN_PESOS, 'Mexican pesos'),
        (COLOMBIAN_PESOS, 'Colombian pesos'),
    ]

    # Implementing choices
    currency = models.CharField(
        _("Currency used in the price"),
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=DOLARS,
        help_text=_(
            "Options for currency are the following 3: USD, MXN or COP"
        ),
        error_messages={
            "choices": _("Only USD, MXN or COP can be passed as currency."),
        }
    )
    
    location = models.CharField(
        _("Location"),
        max_length=3,
        unique=True,
        help_text=_(
            "Floor number and room letter separated by a hyphen. Ex: 3-B"
        ),
        error_messages={
            "unique": _("A room with that location already exists."),
        }
    )

    # Setting a price per night
    price_per_night = models.DecimalField(
        _("Price Per Night"),
        max_digits=6,
        decimal_places=2,
        help_text=_(
            "Enter this room price per night (it can not be more expensive than $9,999.99). Ex: 120.00"
        ),
        error_messages={
            "max_digits": _("Room price can not be more expensive than $9,999.99"),
        }
    )
    is_available = models.BooleanField(
        _("Is this room currently available?"),
        default=True
    )

    def __str__(self):
        return self.location