from django.db import models

# Create your models here.

class office(models.Model):
    employee_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    job_title=models.CharField(max_length=25)
    salary=models.IntegerField()
    reports_to=models.IntegerField()
    office_id=models.IntegerField()