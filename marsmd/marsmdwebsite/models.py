# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)
    reason = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        
        db_table = 'appointment'


class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=45)
    hospital = models.CharField(max_length=45)
    speciality = models.CharField(max_length=45)
    working_hours = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.IntegerField()
    address = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'doctor'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'login'


class MedicalRecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)
    symptoms = models.CharField(max_length=200)
    medicines = models.CharField(max_length=100)
    appointments = models.CharField(max_length=200)
    blogs = models.CharField(max_length=500)

    class Meta:
        
        db_table = 'medical_record'


class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    sex = models.CharField(max_length=45)
    phone = models.IntegerField()
    email = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'patient'
