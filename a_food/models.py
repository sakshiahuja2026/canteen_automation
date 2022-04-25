import email
from email.message import Message
from tkinter import Image
from tokenize import Name
from django.db import models
from datetime import datetime

# Create your models here.


class food(models.Model):
    #fid=models.IntegerField()
    fname=models.CharField(max_length=50,null=True)
    price=models.FloatField(null=True)
    quantity=models.IntegerField(null=True)
    Description=models.CharField(max_length=300,null=True)
    image=models.ImageField(upload_to='food_images')    

    class Meta:
        db_table="a_food"

    def __str__(self):
        return self.fname



class category(models.Model):
    cname=models.CharField(max_length=50)
    cid=models.IntegerField()
    
    class Meta:
        db_table="category"

class removefood(models.Model):
    cid=models.ForeignKey(category,on_delete=models.CASCADE)
    food=models.ForeignKey(food, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    class Meta:
        db_table="removefood"