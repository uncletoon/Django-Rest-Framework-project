from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# def validate_title(value):
#         qs = Product.objects.filter(title__iexact=value)
#         if qs.exists:
#             raise serializers.ValidationError(f" '{value}' title is already exist in database.")
#         return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"No 'hello' Word allowed in Title.")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")