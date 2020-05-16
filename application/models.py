from django.conf import settings
from django.db import models
from django.utils import timezone


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.description


class SubGroup(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def publish(self):
        self.save()

    def __str__(self):
        return "{0} > {1}".format(self.group, self.description)


class Account(models.Model):
    DEFAULT = 'CC'
    INVESTMENT = 'CI'
    ACCOUNT_TYPES_CHOICES = (
        (DEFAULT, 'Padrão'),
        (INVESTMENT, 'Investimento')
    )

    ATIVA = 'A'
    INATIVA = 'I'
    ACCOUNT_STATUS_CHOICES = (
        (ATIVA, 'Ativa'),
        (INATIVA, 'Inativa')
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPES_CHOICES,
        default=DEFAULT,
    )
    description = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    status = models.CharField(
        max_length=1,
        choices=ACCOUNT_STATUS_CHOICES,
        default=ATIVA,
    )
    default = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.description


class Transaction(models.Model):
    CREDITO = 'C'
    DEBITO = 'D'
    TRANSACTION_TYPES_CHOICES = (
        (CREDITO, 'Crédito'),
        (DEBITO, 'Débito')
    )

    ABERTO = 'A'
    LIQUIDADO = 'L'
    TRANSACTION_STATUS_CHOICES = (
        (ABERTO, 'Aberto'),
        (LIQUIDADO, 'Liquidado')
    )
    id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=1,
        choices=TRANSACTION_TYPES_CHOICES,
        default=CREDITO,
    )
    description = models.CharField(max_length=50)
    createOn = models.DateTimeField()
    settlementOn = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    subGroup = models.ForeignKey(SubGroup, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=1,
        choices=TRANSACTION_STATUS_CHOICES,
        default=ABERTO,
    )
    transferId = models.IntegerField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return "{0} > {1} > {2}".format(self.account, self.subGroup, self.description)
