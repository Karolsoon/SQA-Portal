from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Supplier_T1(models.Model):
    name = models.CharField(max_length=100)
    valid_from = models.DateField(timezone.now())
    is_9001 = models.BooleanField(default=False)
    is_17494 = models.BooleanField(default=False)

class Supplier_T2(models.Model):
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=CASCADE)

class Supplier_T3(models.Model):
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=CASCADE)
    supplier_t2 = models.ForeignKey(Supplier_T2, on_delete=CASCADE)

class Subassembly(models.Model):
    part_number = models.CharField(max_length=50)
    part_name = models.CharField(max_length=50)

class Part(models.Model):
    part_name = models.CharField(max_length=50)
    part_number = models.CharField(max_length=30)
    subassy = models.ForeignKey(Subassembly, on_delete=CASCADE)
    supplier_t1 = models.ForeignKey(Supplier_T1, on_delete=models.CASCADE)
    valid_from = models.DateField('validation date')
    is_valid = models.BooleanField(default=False)
    requalification = models.DateField(valid_from)

class PPAP(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=5)
    validated = models.BooleanField(default=False)
