from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from p_library.models import Author, Book, Publisher, Friend
from p_library.forms import AuthorForm, BookForm, PublisherForm, FriendForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'book_edit.html'

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'book_edit.html'

class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

class PublisherUpdate(UpdateView):
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('p_library:publisher_list')
    template_name = 'publisher_edit.html'

class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('p_library:publisher_list')
    template_name = 'publisher_edit.html'

class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'

class FriendUpdate(UpdateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'

class FriendCreate(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_edit.html'

class FriendList(ListView):
    model = Friend
    template_name = 'friend_list.html'

def library(request):
    template = loader.get_template('library.html')
    books = Book.objects.all()
    friends = Friend.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "friends": friends,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            book.copy_count += 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

def borrowed_book(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        friend_id = request.POST['select_borrowed']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            friend = Friend.objects.get(id=friend_id)
            if not book:
                return redirect('/library/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
                book.borrowed_book_count += 1
                book.friend.add(friend)
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

def returned_book(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        friend_id = request.POST['select_returned']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            friend = Friend.objects.get(id=friend_id)
            if not book:
                return redirect('/library/')
            if book.borrowed_book_count < 1:
                book.borrowed_book_count = 0
            else:
                book.copy_count += 1
                book.borrowed_book_count -= 1
                book.friend.remove(friend)
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')

