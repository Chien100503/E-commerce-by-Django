from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('addCart/', views.cart_add, name="cart_add"),
    path('updateCart/', views.cart_update, name="cart_update"),
    path('deleteCart/', views.cart_delete, name="cart_delete"),
]
