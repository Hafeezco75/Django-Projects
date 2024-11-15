from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import Customer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = Customer
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']