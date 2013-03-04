from django.db import models



# Create your models here.
class Repository(models.Model):
  
  # arch choices
  ARCH_CHOICES = (
      ('AMD64', 'amd64'),
      ('I386', 'i386'),
      ('x86_64', 'x86_64'),
  )

  TYPE_CHOICES = (
    ('APT','apt'),
    ('YUM','yum'),
    ('RSYNC','rsync'),
  )
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=5, choices=TYPE_CHOICES)
  url = models.CharField(max_length=256)
  arch = models.CharField(max_length=7, choices=ARCH_CHOICES)

  def __unicode__(self):
    return self.name
