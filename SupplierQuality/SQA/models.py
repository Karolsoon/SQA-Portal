import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Supplier_T1(models.Model):
    name = models.CharField(max_length=60, unique=True, default='Tier1 Supplier')
    valid_from = models.DateField(verbose_name='Supplier validated on', default=timezone.now())
    is_9001 = models.BooleanField(default=False)
    is_17494 = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Supplier_T2(models.Model):
    name = models.CharField(max_length=60, unique=True, default='Tier2 Supplier')
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Supplier_T3(models.Model):
    name = models.CharField(max_length=60, unique=True, default='Tier3 Supplier')
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=CASCADE)
    supplier_t2 = models.ForeignKey(Supplier_T2, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Subassembly(models.Model):
    name = models.CharField(max_length=60, unique=True, default='Subassembly name')
    part_number = models.CharField(max_length=50)
    part_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Part(models.Model):
    part_name = models.CharField(max_length=50, unique=True)
    part_number = models.CharField(max_length=30)
    subassy = models.ForeignKey(Subassembly, on_delete=CASCADE, default=None, null=True, blank=True)
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=models.CASCADE)
    is_produced = models.BooleanField('Is in production' ,default=False)

    def __str__(self):
        return self.part_name


class Claim(models.Model):
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=CASCADE)
    number = models.CharField(max_length=10, unique=True, default='8D YY/XXX')
    part_id =models.ForeignKey(Part, on_delete=CASCADE, default=1)
    supplier_number = models.CharField(blank=True, max_length=50)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(verbose_name='Claim date', default=timezone.now())
    created_by = models.ForeignKey(User, on_delete=CASCADE)
    closed = models.BooleanField(default=False)
    closed_on = models.DateTimeField(verbose_name='Claim closed on', blank=True, null=True)
    
    def give_claim_number(self):
        #Count claims from current year
        #assign next free number
        #Start numbers from 1
        #Represent number as 001
        #Return in form 8D 21/001
        pass

    def set_due_dates(self):
        #Return D3, D6, D8 dates
        pass

    def __str__(self):
        return self.number


class PPAP(models.Model):
    part_id = models.ForeignKey(Part, on_delete=CASCADE, default=1)
    number = models.CharField(max_length=100, default='PPAP -supplier_name- -part_number- -revision- -date-')
    quantity = models.IntegerField(default=5)
    revision = models.CharField(max_length=20, default='0')
    validated = models.BooleanField(default=False)
    valid_from = models.DateField('validation date', null=True, blank=True)
    is_valid = models.BooleanField('Part is validated',default=False)

    def __str__(self):
        return self.number
