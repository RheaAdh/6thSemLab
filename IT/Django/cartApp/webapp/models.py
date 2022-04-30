from django.db import models
from django.db.models.aggregates import Count

class Item(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.IntegerField()


class User(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cash=models.IntegerField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)