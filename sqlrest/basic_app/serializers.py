from rest_framework import serializers
from .models import Employees, Customers, Orders, Products, Orders_Products


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class Orders_ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders_Products
        fields = '__all__'