from django.db import models

# Create your models here.

class Bootoption(models.Model):
  label = models.CharField(max_length=50)
  menu_label = models.CharField(max_length=120) 
  options = models.TextField()

  def __unicode__(self):
    return self.menu_label

class Defaultboot(models.Model):
  menu_name = models.CharField(max_length=120)
  boot_options = models.ManyToManyField(Bootoption, related_name='b+')

  def __unicode__(self):
    return self.menu_name

class Serverboot(models.Model):
  servername = models.CharField(max_length=120)
  macaddress = models.CharField(max_length=50)
  enabled = models.BooleanField(default=True)
  bootoption = models.ForeignKey(Bootoption)

  def __unicode__(self):
    return self.servername

