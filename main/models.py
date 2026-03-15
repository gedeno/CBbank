from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Userprofile(models.Model):
    Username = models.CharField(max_length=100)
    acc_no = models.IntegerField()
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)