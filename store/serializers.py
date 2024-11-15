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

class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price'
    )

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'total_price']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.price * cart_item.quantity


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    total = serializers.SerializerMethodField(
        method_name='get_total_price'
    )

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total']

    def get_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])




#collection = serializers.HyperlinkedRelatedField(
#    queryset=Collection.objects.all(), view_name='collection-detail',
#)


#class Meta:
#    model = Product
#    fields = ['id', 'title', 'price', 'inventory']
