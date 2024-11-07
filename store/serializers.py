from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection, Review, CartItem, Cart


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'product', 'title', 'content']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'items']

#collection = serializers.HyperlinkedRelatedField(
#    queryset=Collection.objects.all(), view_name='collection-detail',
#)


#class Meta:
#    model = Product
#    fields = ['id', 'title', 'price', 'inventory']
