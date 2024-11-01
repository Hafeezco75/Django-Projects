from decimal import Decimal

from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView

from store.models import Product, Collection

#class ProductList(ListCreateAPIView)
    #queryset = Product.objects.all
    #serializer_class = CreateProductSerializer

#class ProductDetailAPIView(RetrieveUpdateDestroyAPIView)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer()
    discount = serializers.SerializerMethodField(method_name='discount_price')

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'discount', 'collection']

    def discount_price(self, product: Product):
        return product.price * Decimal(0.10)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'inventory', 'collection']

#collection = serializers.HyperlinkedRelatedField(
#    queryset=Collection.objects.all(), view_name='collection-detail',
#)



#class Meta:
#    model = Product
#    fields = ['id', 'title', 'price', 'inventory']