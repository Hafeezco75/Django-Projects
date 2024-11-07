from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from store.filters import ProductFilter
from store.models import Product, Collection, Review, CartItem, Cart
from store.serializers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartItemSerializer, \
    CartSerializer


# Create your views here.

#localhost:8000/store/products
#localhost:8000/store/products/1

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination
    #filtersets_fields = ['collection_id', 'title']

class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionUpdateView(RetrieveUpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = PageNumberPagination


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

class CartViewSet(ListCreateAPIView, GenericViewSet, CreateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filter_backends = [DjangoFilterBackend]


#class ProductListView(CreateListMixin)
#   queryset = Product.objects.all()
#   serializer = CreateProductSerializer


#@api_view()
#def collection_list(request):
#    collectionsAll = Collection.objects.all()
#    serializer = CollectionSerializer(collectionsAll, many=True)
#    return Response(serializer.data, status=status.HTTP_200_OK)


#@api_view()
#def collection_detail(request, pk):
#    collectionList = get_object_or_404(Collection, pk=pk)
#    serializer = CollectionSerializer(collectionList)
#    return Response(serializer.data, status=status.HTTP_200_OK)


#@api_view(['GET', 'PUT', 'DELETE'])
#def products(request, pk):
#    productList = get_object_or_404(Product, pk=pk)
#    if request.method == 'GET':
#        serializer = ProductSerializer(productList)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    if request.method == 'PUT':
#        serializer = CreateProductSerializer(productList, data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#   if request.method == 'DELETE':
#       productList.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

#@api_view(['GET', 'POST'])
#def product(request):
#    if request.method == 'GET':
#       productsAll = Product.objects.all()
#      serializer = ProductSerializer(productsAll, many=True)  #context={"request": request}
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    elif request.method == 'POST':
#       serializer = CreateProductSerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
