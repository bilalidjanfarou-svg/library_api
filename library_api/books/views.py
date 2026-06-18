from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
import django_filters as df
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly

class BookFilter(df.FilterSet):
    class Meta:
        model = Book
        fields = ['available', 'published_year', 'category']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]






    