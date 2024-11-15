from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from user.models import Customer



# Create your views here.


class UserRegisterViewSet(CreateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()

