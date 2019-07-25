from django.shortcuts import render

# Create your views here.
from pqrs.serializers import BooksSerializer
from pqrs.models import Books
from rest_framework.viewsets import ModelViewSet


class BookOperations(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
