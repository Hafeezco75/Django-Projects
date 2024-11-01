from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product, Collection
from store.serializers import ProductSerializer, CollectionSerializer, CreateProductSerializer


# Create your views here.

#localhost:8000/store/products
#localhost:8000/store/products/1

@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        productsAll = Product.objects.all()
        serializer = ProductSerializer(productsAll, many=True)  #context={"request": request}
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def products(request, pk):
    productList = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(productList)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CreateProductSerializer(productList, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        productList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def collection_list(request):
    collectionsAll = Collection.objects.all()
    serializer = CollectionSerializer(collectionsAll, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def collection_detail(request, pk):
    collectionList = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collectionList)
    return Response(serializer.data, status=status.HTTP_200_OK)




