from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(
        _("E-mail"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        }
    )
    phone = models.CharField(
        _("Phone Number"),
        max_length=12,
        unique=True,
        error_messages={
            "unique": _("A user with that phone number already exists."),
        }
    )
    # Tax identification number used for billing
    tax = models.CharField(
        _("Tax Identification Number"),
        max_length=10,
        unique=True,
        help_text=_(
            "8 (eight) numbers and 1 (one) letter separated by a hyphen. Ex: 12345678-A"
        ),
        error_messages={
            "unique": _("A user with that tax identification number already exists."),
        }
    )
    address = models.CharField(
        _("Address"),
        max_length=300
    )

    def __str__(self):
        return self.username