from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Omo(models.Model):
    battery =models.IntegerField(null=True, default=0)
    bat_status = models.CharField(max_length=10, null=True, default="on")
    r_led = models.IntegerField(null=True, default=0)
    g_led = models.IntegerField(null=True, default=0)
    b_led = models.IntegerField(null=True, default=0)
    r_rpm = models.IntegerField(null=True, default=0)
    l_rpm = models.IntegerField(null=True, default=0)
    buzzer =models.CharField(max_length=10,null=True, default="off")
    headlight = models.CharField(max_length=10,null=True, default="off")
    content = models.TextField(null=True, default="")
    created_at =models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, null=True, default="")
    writer =models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
     
    
    def __str__(self):
        return f'{self.pk}'

class PredResults(models.Model):
    battery = models.IntegerField(null=True)
    rpm = models.IntegerField(null=True)
    headlight = models.IntegerField(null=True)
    buzzer = models.IntegerField(null=True)
    led = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'[{self.pk}]{self.led}'









        

    

    







