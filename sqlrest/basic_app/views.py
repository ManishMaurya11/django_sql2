from django.shortcuts import render
from .models import Employees, Customers, Orders, Products, Orders_Products
from .serializers import EmployeesSerializer, CustomersSerializer, OrdersSerializer, ProductsSerializer, Orders_ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import Http404


# Create your views here.

# Employees -------------------------------------------------------------------

class EmployeesAPIView(APIView):

    def get(self,request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeesDetails(APIView):

    def get_object(self,pk):
        try:
            employees = Employees.objects.get(pk=pk)
            return employees

        except Employees.DoesNotExist:
            raise Http404
            #return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


# Customers -------------------------------------------------------

class CustomersAPIView(APIView):

    def get(self,request):
        employees = Customers.objects.all()
        serializer = CustomersSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CustomersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomersDetails(APIView):

    def get_object(self,pk):
        try:
            employees = Customers.objects.get(pk=pk)
            return employees

        except Customers.DoesNotExist:
            raise Http404
            #return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = CustomeresSerializer(employees)
        return Response(serializer.data)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = CustomersSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


# Orders----------------------------------------------------------------------------


class OrdersAPIView(APIView):

    def get(self,request):
        employees = Orders.objects.all()
        serializer = OrdersSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = OrdersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersDetails(APIView):

    def get_object(self,pk):
        try:
            employees = Orders.objects.get(pk=pk)
            return employees

        except Orders.DoesNotExist:
            raise Http404
            #return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = OrdersSerializer(employees)
        return Response(serializer.data)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = OrdersSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)



# Products--------------------------------------------------------------------

class ProductsAPIView(APIView):

    def get(self,request):
        employees = Products.objects.all()
        serializer = ProductsSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsDetails(APIView):

    def get_object(self,pk):
        try:
            employees = Products.objects.get(pk=pk)
            return employees

        except Products.DoesNotExist:
            raise Http404
            #return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = ProductsSerializer(employees)
        return Response(serializer.data)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = ProductsSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)



# Order_Products--------------------------------------------------------------------

class Orders_ProductsAPIView(APIView):

    def get(self,request):
        employees = Orders_Products.objects.all()
        serializer = Orders_ProductsSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Orders_ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Orders_ProductsDetails(APIView):

    def get_object(self,pk):
        try:
            employees = Orders_Products.objects.get(pk=pk)
            return employees

        except Orders_Products.DoesNotExist:
            raise Http404
            #return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = Orders_ProductsSerializer(employees)
        return Response(serializer.data)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = Orders_ProductsSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)