from rest_framework import viewsets
from .serializers import book_serializer
from .models import books_table

# Create your views here.
class book_viewset(viewsets.ModelViewSet):
    serializer_class = book_serializer
    queryset = books_table.objects.all()