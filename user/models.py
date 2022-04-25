import email
from email.message import Message
from tokenize import Name
from datetime import datetime
from django.db import models

class reservation(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Date=models.DateField(default=datetime.utcnow)
    Time=models.TimeField()
    Number=models.IntegerField()

    class Meta:
        db_table="reservation"

class contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Number_people=models.IntegerField()
    Message=models.CharField(max_length=200, null=True)

    class Meta:
        db_table="contact"