from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import BookReviewForm
from books.models import Book, BookReview


class BookView(ListView):
    model = Book
    template_name = 'book/books.html'


class BookDetail(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()

        return render(request, "book/detail.html", {"book": book, "review_form": review_form})


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                comment=review_form.cleaned_data['comment']
            )

            return redirect(reverse('detail', kwargs={'id': book.id}))

        return render(request, "book/detail.html", {"book": book, "review_form": review_form})