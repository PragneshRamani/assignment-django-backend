import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserBalance(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("User Balance")
        verbose_name_plural = _("User Balances")


class UserTransaction(models.Model):
    TRANSACTION_TYPE = (
        ('Borrows', _('Borrows')),
        ('Lendes', _('Lendes')),
    )
    TRANSACTION_STATUS = (
        ('Unpaid', _('Unpaid')),
        ('Paid', _('Paid')),
    )
    transaction_from = models.ForeignKey(User, 
                            related_name='transaction_from_user',
                            null=True,
                            on_delete=models.SET_NULL)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    transaction_type = models.CharField(max_length=128, choices=TRANSACTION_TYPE, null=True, blank=True)
    transaction_date = models.DateTimeField(default=None, null=True, blank=True)
    transaction_status = models.CharField(max_length=128, choices=TRANSACTION_STATUS, null=True, blank=True)
    transaction_with = models.ForeignKey(User, 
                            related_name='transaction_with_user',
                            blank=True, null=True,
                            on_delete=models.SET_NULL)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_id}"

    class Meta:
        verbose_name = _("User Transaction")
        verbose_name_plural = _("User Transactions")