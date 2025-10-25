from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    title = serializers.CharField(validators=[validators.unique_product_title, validators.validate_title_no_hello])

    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
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