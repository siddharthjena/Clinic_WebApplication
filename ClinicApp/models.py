from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Storing password as plain text for simplicity

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time}"
   

