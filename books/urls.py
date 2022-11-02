from django.urls import path
from .views import BookView, BookDetail, AddReviewView

urlpatterns = [
    path("", BookView.as_view(), name='books'),
    path("<int:id>/", BookDetail.as_view(), name='detail'),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="reviews"),
]



