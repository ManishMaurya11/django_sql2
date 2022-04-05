from django.urls import path
from .views import EmployeesAPIView, EmployeesDetails, CustomersAPIView, CustomersDetails, OrdersAPIView, OrdersDetails, ProductsAPIView, ProductsDetails, Orders_ProductsAPIView, Orders_ProductsDetails

urlpatterns = [
    path('employees/',EmployeesAPIView.as_view()),
    path('employees/<int:pk>/',EmployeesDetails.as_view()),
    path('customers/',CustomersAPIView.as_view()),
    path('customers/<int:pk>/',CustomersDetails.as_view()),
    path('orders/',OrdersAPIView.as_view()),
    path('orders/<int:pk>/',OrdersDetails.as_view()),
    path('products/',ProductsAPIView.as_view()),
    path('products/<int:pk>/',ProductsDetails.as_view()),
    path('orders_products/',Orders_ProductsAPIView.as_view()),
    path('orders_products/<int:pk>/',Orders_ProductsDetails.as_view()),
]

