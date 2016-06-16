from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Operation(models.Model):
    first_number = models.FloatField()
    operator_choice = models.CharField(max_length=2)
    second_number = models.FloatField()
    result = models.FloatField()
    user = models.ForeignKey(User)
