from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=40)
    past_job = models.TextField()
   
    
  