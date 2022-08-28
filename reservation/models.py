from django.db import models
from django.utils.translation import gettext_lazy as _
from room.models import Room
from user.models import User
import uuid

class Reservation(models.Model):

    # Setting choices to be used as reservation status
    PENDING = 'PNDG'
    PAID = 'PAID'
    REMOVED = 'RMVD'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (REMOVED, 'Removed'),
    ]

    # Implementing choices
    status = models.CharField(
        _("Status"),
        max_length=4,
        choices=STATUS_CHOICES,
        default=PENDING,
        help_text=_(
            "Options for currency are the following 3: 'PNDG' for pending status, 'PAID' for paid status or 'RMVD' for removed status"
        ),
        error_messages={
            "choices": _("Only 'PNDG' for pending status, 'PAID' for paid status or 'RMVD' for removed status can be passed as status."),
        }
    )

    # Setting choices to be used as payment method
    EFFECTIVE = 'EFF'
    DEBIT_CARD = 'DBT'
    CREDIT_CARD = 'CDT'
    PAYMENT_METHOD_CHOICES = [
        (EFFECTIVE, 'Effective cash'),
        (DEBIT_CARD, 'Debit card'),
        (CREDIT_CARD, 'Credit card'),
    ]

    # Implementing choices
    payment_method = models.CharField(
        _("Payment method"),
        max_length=3,
        choices=PAYMENT_METHOD_CHOICES,
        help_text=_(
            "Options for payment method are the following 3: 'EFF' for effective cash, 'DBT' for debit card or 'CDT' for credit card"
        ),
        error_messages={
            "choices": _("Only 'EFF' for effective cash, 'DBT' for debit card or 'CDT' for credit card can be passed as payment method."),
        }
    )

    # Crating a secondary unique key to be showed instead of ID
    uuid = models.UUIDField(
        editable=False,
        unique=True,
        default=uuid.uuid4()
    )

    # Setting a relation between reservation and room reservated
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        help_text=_(
            "Pass here room room ID"
        ),
    )

    # Setting a relation between reservation and its owner
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_(
            "If client has not created a client account yet, you need to create it, then pass their ID in this field"
        ),
    )

    days_of_stay = models.IntegerField(
        _("Days of Stay")
    )

    total_price = models.CharField(
        _("Total price"),
        max_length=16,
        blank=True,
        help_text=_(
            "You can leave this field blank, it will be self-calculated"
        ),
    )

    def __str__(self):
        return self.uuid
