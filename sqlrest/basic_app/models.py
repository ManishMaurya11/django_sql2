from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Customers(models.Model):
    cust_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    cust_id = models.ForeignKey(Customers, on_delete=models.DO_NOTHING)
    order_date = models.DateField()
    emp_id = models.ForeignKey(Employees, on_delete=models.DO_NOTHING)

class Products(models.Model):
    prod_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    units_remain = models.IntegerField()
    unit_price = models.IntegerField()
    order_id = models.ManyToManyField(Orders, through='Orders_Products')


class Orders_Products(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    units = models.IntegerField()



