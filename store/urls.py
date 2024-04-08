from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about),
    path('services/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    
]
