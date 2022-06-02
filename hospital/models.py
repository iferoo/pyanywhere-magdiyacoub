from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os

# Create your models here.


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"media/patientsimage/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class Room(models.Model):
    Name = models.CharField(max_length=70, null=True)


class Bed(models.Model):
    RoomID = models.ForeignKey(
        Room, related_name='Beds', on_delete=models.CASCADE)


class Doctor(models.Model):
    Name = models.CharField(max_length=70, null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=70, null=True)
    Email = models.EmailField(max_length=70, null=True)
    Status = models.CharField(max_length=70, null=True)


class Nurse(models.Model):
    Name = models.CharField(max_length=70, null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=70, null=True)
    Email = models.EmailField(max_length=70, null=True)
    Status = models.CharField(max_length=70, null=True)


class Patient(models.Model):
    Img = models.ImageField(_("ProposalItemImage"),
                            upload_to=upload_to, blank=True)
    Name = models.CharField(max_length=70, null=True)
    Bed = models.OneToOneField(
        Bed, on_delete=models.SET_NULL, related_name='Patient', null=True)
    Status = models.CharField(max_length=70, null=True)
    Condition = models.CharField(max_length=70, null=True)
    Age = models.CharField(max_length=70, null=True)
    Gender = models.CharField(max_length=70, null=True)
    RegisterDate = models.DateField(max_length=70, null=True)
    Branch = models.CharField(max_length=70, null=True)
    Nurse = models.ForeignKey(
        Nurse, related_name='PatientNurse', on_delete=models.CASCADE)
    Doctor = models.ForeignKey(
        Doctor, related_name='PatientDoctor', on_delete=models.CASCADE)
    Disease = models.CharField(max_length=70, null=True)
    History = models.DateField(max_length=70, null=True)
    OtherDiseases = models.CharField(max_length=70, null=True)
    Diabeyic = models.BooleanField(max_length=70, null=True)
    Smoker = models.BooleanField(max_length=70, null=True)
