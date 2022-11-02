from django.contrib import admin
from .models import Book, BookReview


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')


admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookAdmin)
