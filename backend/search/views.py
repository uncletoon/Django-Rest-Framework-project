from rest_framework import generics

from api.mixins import StaffEditorPermissionMixin

from products. models import Product
from products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        query = self.request.query_params.get('q')
        user = self.request.user if self.request.user.is_authenticated else None
        """
        Or
        if self.request.user.is_authenticated:
            user = sself.request.user
        else:
            None.
        """
        if query:
            return Product.objects.search(query, user=user)
        return Product.objects.none()
        