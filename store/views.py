from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from store.serializers import ProductSerializer


# Create your views here.

#localhost:8000/store/products
#localhost:8000/store/products/1

@api_view()
def product(request):
    productsAll = Product.objects.all()
    serializer = ProductSerializer(productsAll, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def products(request, pk):
    productList = Product.objects.get(pk=pk)
    serializer = ProductSerializer(productList)
    return Response(serializer.data, status=status.HTTP_200_OK)


