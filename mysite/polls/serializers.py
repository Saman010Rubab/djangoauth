from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image']

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError("Product name is required.")
        if not data.get('image'):
            raise serializers.ValidationError("Product image is required.")
        return data

