from rest_framework import serializers
from .models import Category,Todo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
            )