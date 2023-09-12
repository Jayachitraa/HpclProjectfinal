# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contractemployee(models.Model):
    emp_id = models.BigIntegerField(primary_key=True)
    emp_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    quali = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    desg = models.CharField(max_length=255, blank=True, null=True)
    ven_code = models.CharField(max_length=10, blank=True, null=True)
    basic = models.CharField(max_length=10, blank=True, null=True)
    doj = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    add1 = models.CharField(max_length=255, blank=True, null=True)
    add2 = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    mob = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    esic_enrolled = models.CharField(max_length=25, blank=True, null=True)
    esic_location = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contractemployee'
