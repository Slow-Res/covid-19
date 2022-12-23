from django.db import models

# Create your models here.
class Country(models.Model):
    country=models.CharField(max_length=255,null=False)
    total_confirmed_cases=models.CharField(max_length=255,null=False)
    total_deaths_cases=models.CharField(max_length=255,null=False)
    total_recovered_cases=models.CharField(max_length=255,null=False)
    Date=models.DateTimeField(auto_now_add=False,null=False)