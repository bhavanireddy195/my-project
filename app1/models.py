from django.db import models

# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('student', 'Student'),
        ('employee', 'Employee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    specialization = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    details = models.TextField()

    def _str_(self):
        return self.name
