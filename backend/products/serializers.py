from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    
    # email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'email',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'related_products',
        ]
   
    # def validate_title(self, value): # it moved into own file called validators.py
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists:
    #         raise serializers.ValidationError(f" '{value}' title is already exist in database.")
    #     return value

    def get_url(self, obj): #Reverse
        request = self.context.get("request")
        if request is None:
            return None
        url = reverse('product-detail', args=[obj.pk], request=request)
        return url
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()