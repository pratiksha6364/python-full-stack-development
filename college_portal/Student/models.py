from django.db import models

# Create your models here.
class Student_table(models.Model):
  regno=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=20)
  email=models.EmailField(default='example@gmail.com')
  marks = models.DecimalField(max_digits=5, decimal_places=2)
  dob=models.DateField()

