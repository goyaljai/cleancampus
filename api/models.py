from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):

    user = models.OneToOneField(User)
    phone_no = models.IntegerField(max_length=10)

    def __str__ (self):
        return self.user.username


class Complaint(models.Model):
    STATUS_CHOICES = (
        (0, "running"),
        (1, "complete"),
        (2, "pending")
    )
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField(default=date.today(), blank=True)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2) # 0 for running , 1 for complete , 2 for pending
    image = models.ImageField(upload_to='images/' , default='images/1.jpg')
    # photo field afterwords

