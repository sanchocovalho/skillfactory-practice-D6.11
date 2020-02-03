from django.urls import path
from p_library import views

app_name = "p_library"

urlpatterns = [
    path('', views.BookList.as_view(), name="book_list"),
    path('create', views.BookCreate.as_view(), name="book_create"),
    path("update<int:pk>", views.BookUpdate.as_view(), name="book_update"),
    path('library/', views.library, name='library'),
    path('library/book_increment/', views.book_increment),
    path('library/book_decrement/', views.book_decrement),
    path('library/borrowed_book/', views.borrowed_book),
    path('library/returned_book/', views.returned_book),
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/create', views.AuthorCreate.as_view(), name='author_create'),
    path("authors/update<int:pk>", views.AuthorUpdate.as_view(), name="author_update"),
    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('publishers/create', views.PublisherCreate.as_view(), name='publisher_create'),
    path("publishers/update<int:pk>", views.PublisherUpdate.as_view(), name="publisher_update"),
    path('friends/', views.FriendList.as_view(), name='friend_list'),
    path('friends/create', views.FriendCreate.as_view(), name='friend_create'),
    path("friends/update<int:pk>", views.FriendUpdate.as_view(), name="friend_update"),
]
