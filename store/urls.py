from django.urls import path

from . import views

urlpatterns = [
    path('product', views.product),
    path('products/<int:pk>/', views.products),
]
