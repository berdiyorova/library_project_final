from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, BookDetailApiView, BookUpdateApiView, BookDeleteApiView, \
    BookCreateApiView, BookListCreateApiView, BookUpdateDeleteView, BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view(),),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/list/create/', BookListCreateApiView.as_view()),
    #
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/updatedelete', BookUpdateDeleteView.as_view()),
]

urlpatterns = urlpatterns + router.urls
