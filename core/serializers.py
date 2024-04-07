from rest_framework import serializers
from .models import books_table

class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = books_table
        fields = '__all__'