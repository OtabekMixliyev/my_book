from rest_framework.generics import ListAPIView
from api.serializer import BookSerializer
from books.models import Book


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
