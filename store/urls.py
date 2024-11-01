from django.urls import path

from . import views

urlpatterns = [
    path('product', views.product),

    path('products/<int:pk>/', views.products), #views.ListProductAsView()


    path('collection', views.collection_list),

    path('collections/<int:pk>/', views.collection_detail), #name='collection_detail'#),
]
