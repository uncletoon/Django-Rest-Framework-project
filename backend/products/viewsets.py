from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermission

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission,]