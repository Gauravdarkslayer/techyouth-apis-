from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=40)
    emailid=models.CharField(max_length=40)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.username