from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter


from . import views

route = DefaultRouter()
route.register("products", views.ProductViewSet, basename='products')
route.register("collections", views.CollectionViewSet, basename='collections')
route.register("carts", views.CartViewSet, basename='carts')
route.register("cartitems", views.CartItemViewSet, basename='cart-items')

product_router = NestedDefaultRouter(route, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


print(route.urls)

urlpatterns = [
    path('', include(route.urls)),

    path('', include(product_router.urls)),
]

#path('collections/<int:pk>/', views.CollectionUpdateView.as_view()), #name='collection_detail'#),

#path('collection', views.CollectionList.as_view()),

#path('products/<int:pk>/', views.products), #views.ListProductAsView()

#print(route.urls)
